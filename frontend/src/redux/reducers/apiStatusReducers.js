import actionTypes from "../actionTypes";

export default function apiStatusReducers(state = 0, action) {
  const endsWithSuccess = action.type.endsWith("_SUCCESS");

  if (action.type === actionTypes.START_API_CALL) {
    return state + 1;
  } else if (endsWithSuccess) {
    return state - 1;
  }
  return state;
}
