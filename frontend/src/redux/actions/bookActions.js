import * as bookApi from "../../api/bookApi";
import actionTypes from "../actionTypes";
import { startApiCall } from "./apiStatusActions";

export function loadBooksSuccess(books = []) {
  return {
    type: actionTypes.LOAD_BOOKS_SUCCESS,
    books,
  };
}

// Thunks
export function loadBooks() {
  return function (dispatch) {
    dispatch(startApiCall());
    return bookApi
      .getBooks()
      .then((books) => {
        dispatch(loadBooksSuccess(books.data.results));
      })
      .catch((error) => {
        // throw error;
      });
  };
}
