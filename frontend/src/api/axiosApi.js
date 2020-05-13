import axios from "axios";
import { baseUrl } from "./baseUrl";

const accessToken = localStorage.getItem("access_token");

const axiosInstance = axios.create({
  baseURL: baseUrl,
  timeout: 5000,
  headers: {
    Authorization: accessToken ? "JWT " + accessToken : null,
    "Content-Type": "application/json",
    accept: "application/json",
  },
});

axiosInstance.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config;

    // Prevent infinite loops
    if (
      error.response.status === 401 &&
      originalRequest.url === baseUrl + "token/refresh/"
    ) {
      window.location.href = "/login/";
      return Promise.reject(error);
    }

    if (
      error.response.status === 401 &&
      error.response.statusText === "Unauthorized"
    ) {
      const refresh = localStorage.getItem("refresh_token");

      if (refresh) {
        const tokenParts = JSON.parse(atob(refresh.split(".")[1]));

        // exp date in token is expressed in seconds, while now() returns milliseconds:
        const now = Math.ceil(Date.now() / 1000);

        if (tokenParts.exp > now) {
          try {
            const response = await axiosInstance.post("users/token/refresh/", {
              refresh,
            });
            setNewHeaders(response);
            originalRequest.headers["Authorization"] =
              "JWT " + response.data.access;
            return axiosInstance(originalRequest);
          } catch (error) {
            console.log(error);
          }
        } else {
          console.log("Refresh token is expired", tokenParts.exp, now);
          window.location.href = "/login/";
        }
      } else {
        console.log("Refresh token not available.");
        window.location.href = "/login/";
      }
    }

    // specific error handling done elsewhere
    return Promise.reject(error);
  }
);

export function setNewHeaders(response) {
  axiosInstance.defaults.headers["Authorization"] =
    "JWT " + response.data.access;
  localStorage.setItem("access_token", response.data.access);
  localStorage.setItem("refresh_token", response.data.refresh);
}

export default axiosInstance;
