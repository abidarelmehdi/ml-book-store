import actionTypes from "../actionTypes";

export default function bookReducers(state = [], action) {
  switch (action.type) {
    case actionTypes.LOAD_BOOKS_SUCCESS:
      return action.books;

    default:
      return state;
  }
}
