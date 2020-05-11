import * as userApi from "../../api/userApi";
import actionTypes from "../actionTypes";
import { startApiCall } from "./apiStatusActions";
import axiosAPI from "../../api/axiosApi";

export function loginSuccess(auth = {}) {
  return {
    type: actionTypes.LOGIN_SUCCESS,
    auth,
  };
}

// Thunks
export function login({ username, password }) {
  return function (dispatch) {
    dispatch(startApiCall());
    return userApi
      .login(username, password)
      .then((res) => {
        axiosAPI.defaults.headers["Authorization"] = "JWT " + res.data.access;
        localStorage.setItem("access_token", res.data.access);
        localStorage.setItem("refresh_token", res.data.refresh);
        dispatch(
          loginSuccess({
            access_token: res.data.access,
            refresh_token: res.data.refresh,
            is_authenticated: true,
          })
        );
      })
      .catch((error) => {
        throw error;
      });
  };
}
