import * as userApi from "../../api/userApi";
import actionTypes from "../actionTypes";
import { startApiCall } from "./apiStatusActions";
import { setNewHeaders } from "../../api/axiosApi";

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
      .then((response) => {
        setNewHeaders(response);
        dispatch(
          loginSuccess({
            access_token: response.data.access,
            refresh_token: response.data.refresh,
            username: response.data.username,
            is_authenticated: true,
          })
        );
      })
      .catch((error) => {
        console.log(error);
      });
  };
}
