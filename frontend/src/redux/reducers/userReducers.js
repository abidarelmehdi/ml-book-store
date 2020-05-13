import actionTypes from "../actionTypes";

const initiateState = {
  access_token: localStorage.getItem("access_token"),
  refresh_token: localStorage.getItem("refresh_token"),
  username: "",
  is_authenticated: !!localStorage.getItem("access_token"),
};

export default function authReducers(state = initiateState, action) {
  switch (action.type) {
    case actionTypes.LOGIN_SUCCESS:
      return action.user;
    default:
      return state;
  }
}
