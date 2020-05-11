import { combineReducers } from "redux";
import books from "./bookReducers";
import auth from "./authReducers";
import apiStatus from "./apiStatusReducers";

const rootReducer = combineReducers({
  books,
  apiStatus,
  auth,
});

export default rootReducer;
