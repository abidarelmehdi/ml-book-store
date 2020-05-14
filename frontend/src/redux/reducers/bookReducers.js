import actionTypes from "../actionTypes";

const initiateState = {
  next: "",
  previous: "",
  count: 0,
  results: [],
};

export default function bookReducers(state = initiateState, action) {
  switch (action.type) {
    case actionTypes.LOAD_BOOKS_SUCCESS:
      return action.books;

    default:
      return state;
  }
}
