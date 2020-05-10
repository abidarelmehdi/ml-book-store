import React, { useState, useEffect } from "react";
import { connect } from "react-redux";
import { loadBooks } from "../../redux/actions/bookActions";
import BookDetailItem from "../books/BookDetailItem";

function BookDetailPage({ loadBooks, books, selectedBook }) {
  const [book, setBook] = useState({
    authors: [],
    categories: [],
  });

  useEffect(() => {
    books.length === 0 && loadBooks();
    selectedBook && setBook(selectedBook);
  }, [loadBooks, books, selectedBook]);

  return (
    <div className="max-w-7xl mx-auto">
      <BookDetailItem book={book} />
    </div>
  );
}

const mapStateToProps = (state, ownProps) => {
  const id = ownProps.match.params.id;
  const selectedBook = state.books.find((book) => book.id === id) || null;
  return {
    selectedBook,
    books: state.books,
  };
};

const mapDispatchToProps = {
  loadBooks,
};
export default connect(mapStateToProps, mapDispatchToProps)(BookDetailPage);
