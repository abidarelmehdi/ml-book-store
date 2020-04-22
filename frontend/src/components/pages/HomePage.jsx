import React, { useEffect } from "react";
import { connect } from "react-redux";
import * as bookActions from "../../redux/actions/bookActions";
import BooksList from "../books/BooksList";

function Home({ setTitle, books, loadBooks }) {
  useEffect(() => {
    setTitle("Home Page");
    books.length === 0 && loadBooks();
  }, [books.length, loadBooks, setTitle]);
  return <BooksList books={books} />;
}

function mapStateToProps(state) {
  return {
    loading: state.apiStatus > 0,
    books: state.books,
  };
}

const mapDispatchToProps = {
  loadBooks: bookActions.loadBooks,
};
export default connect(mapStateToProps, mapDispatchToProps)(Home);
