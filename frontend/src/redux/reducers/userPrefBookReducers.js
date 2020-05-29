import actionTypes from "../actionTypes";

const initiateState = [];

export default function userPrefBookReducers(state = initiateState, action) {
  switch (action.type) {
    case actionTypes.LOAD_USER_PREF_BOOKS_SUCCESS:
      return action.userPrefBooks;

    default:
      return state;
  }
}
