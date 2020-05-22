import { combineReducers } from "redux";
import books from "./bookReducers";
import ratedBooks from "./ratedBooksReducers";
import user from "./userReducers";
import apiStatus from "./apiStatusReducers";

const rootReducer = combineReducers({
  books,
  ratedBooks,
  apiStatus,
  user,
});

export default rootReducer;
