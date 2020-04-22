import { combineReducers } from "redux";
import books from "./bookReducers";
import apiStatus from "./apiStatusReducers";

const rootReducer = combineReducers({
  books,
  apiStatus,
});

export default rootReducer;
