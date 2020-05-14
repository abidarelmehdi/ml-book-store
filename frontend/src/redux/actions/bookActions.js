import * as bookApi from "../../api/bookApi";
import actionTypes from "../actionTypes";
import { startApiCall } from "./apiStatusActions";

export function loadBooksSuccess(books = {}) {
  return {
    type: actionTypes.LOAD_BOOKS_SUCCESS,
    books,
  };
}

export function getBookByIdSuccess(book = {}) {
  return {
    type: actionTypes.GET_BOOK_BY_ID_SUCCESS,
    book,
  };
}

// Thunks
export function loadBooks(querySTring) {
  return function (dispatch) {
    dispatch(startApiCall());
    return bookApi
      .getBooks(querySTring)
      .then((res) => {
        dispatch(loadBooksSuccess(res.data));
      })
      .catch((error) => {
        // throw error;
      });
  };
}

export function getBookById(id) {
  return function (dispatch) {
    dispatch(startApiCall());
    return bookApi
      .getBookbyId(id)
      .then((book) => {
        dispatch(getBookByIdSuccess(book.data));
      })
      .catch((error) => {
        // throw error;
      });
  };
}
