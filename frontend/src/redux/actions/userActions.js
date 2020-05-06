import * as userApi from "../../api/userApi";
import actionTypes from "../actionTypes";
import { startApiCall } from "./apiStatusActions";

export function loginSuccess(user = {}) {
  return {
    type: actionTypes.LOGIN_SUCCESS,
    user,
  };
}

// Thunks
export function login({ username, password }) {
  return function (dispatch) {
    dispatch(startApiCall());
    return userApi
      .login(username, password)
      .then((user) => {
        dispatch(
          loginSuccess({
            username,
            ...user.data,
          })
        );
      })
      .catch((error) => {
        throw error;
      });
  };
}
