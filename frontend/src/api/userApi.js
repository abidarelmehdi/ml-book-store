import { baseUrl } from "./baseUrl";
import axios from "./axiosApi";

export function login(username, password) {
  return axios
    .post(baseUrl + "users/token/obtain/", {
      username,
      password,
    })
    .catch((err) => console.log(err));
}
