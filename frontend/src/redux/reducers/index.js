import { combineReducers } from "redux";
import books from "./bookReducers";
import apiStatus from "./apiStatusReducers";
import user from "./userReducers";

const rootReducer = combineReducers({
  books,
  apiStatus,
  user,
});

export default rootReducer;
