import * as bookApi from "../../api/bookApi";
import actionTypes from "../actionTypes";
import { startApiCall } from "./apiStatusActions";

export function loadUserPrefBooksSuccess(userPrefBooks = []) {
  return {
    type: actionTypes.LOAD_USER_PREF_BOOKS_SUCCESS,
    userPrefBooks,
  };
}

// Thunks
export function loadUserPrefBooks() {
  return function (dispatch) {
    dispatch(startApiCall());
    return bookApi
      .getUserPreferenceBooks()
      .then((res) => {
        dispatch(loadUserPrefBooksSuccess(res.data));
      })
      .catch((error) => {
        throw error;
      });
  };
}
