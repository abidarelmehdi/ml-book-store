import actionTypes from "../actionTypes";

export default function userReducers(state = {}, action) {
  switch (action.type) {
    case actionTypes.LOGIN_SUCCESS:
      return action.user;
    default:
      return state;
  }
}
