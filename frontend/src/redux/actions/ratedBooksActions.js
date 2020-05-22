import * as bookApi from "../../api/bookApi";
import actionTypes from "../actionTypes";
import { startApiCall } from "./apiStatusActions";

export function loadRatedBooksSuccess(ratedBooks = {}) {
  return {
    type: actionTypes.LOAD_RATED_BOOKS_SUCCESS,
    ratedBooks,
  };
}

// Thunks
export function loadRatedBooks() {
  return function (dispatch) {
    dispatch(startApiCall());
    return bookApi
      .getUserRatedBooks()
      .then((res) => {
        dispatch(loadRatedBooksSuccess(res.data));
      })
      .catch((error) => {
        throw error;
      });
  };
}
