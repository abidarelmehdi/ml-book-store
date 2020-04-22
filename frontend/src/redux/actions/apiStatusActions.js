import actionTypes from "../actionTypes";

export function startApiCall() {
  return {
    type: actionTypes.START_API_CALL,
  };
}
