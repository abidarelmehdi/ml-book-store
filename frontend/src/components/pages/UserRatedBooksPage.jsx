import React, { useEffect } from "react";
import { connect } from "react-redux";
import * as bookActions from "../../redux/actions/bookActions";
import BooksList from "../books/BooksList";

function UserRatedBooksPage({ books, loadBooks }) {
  useEffect(() => {
    loadBooks();
  }, [loadBooks]);
  return <></>;
}

function mapStateToProps(state) {
  return {
    loading: state.apiStatus > 0,
    books: state.books,
  };
}

const mapDispatchToProps = {
  loadBooks: bookActions.loadRatedBooks,
};
export default connect(mapStateToProps, mapDispatchToProps)(UserRatedBooksPage);
