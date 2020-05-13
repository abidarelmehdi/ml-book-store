import { combineReducers } from "redux";
import books from "./bookReducers";
import user from "./userReducers";
import apiStatus from "./apiStatusReducers";

const rootReducer = combineReducers({
  books,
  apiStatus,
  user,
});

export default rootReducer;
