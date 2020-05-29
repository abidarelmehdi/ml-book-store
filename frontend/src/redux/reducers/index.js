import { combineReducers } from "redux";
import books from "./bookReducers";
import userPrefBooks from "./userPrefBookReducers";
import ratedBooks from "./ratedBooksReducers";
import user from "./userReducers";
import apiStatus from "./apiStatusReducers";

const rootReducer = combineReducers({
  books,
  userPrefBooks,
  ratedBooks,
  apiStatus,
  user,
});

export default rootReducer;
