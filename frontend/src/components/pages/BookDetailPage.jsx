import React, { useState, useEffect } from "react";
import { getBookbyId } from "../../api/bookApi";
import BookDetailItem from "../books/BookDetailItem";

function BookDetailPage({ match }) {
  const [book, setBook] = useState({
    authors: [],
    categories: [],
  });

  useEffect(() => {
    getBookbyId(match.params.id).then((_book) => setBook(_book.data));
  }, [match.params.id]);

  return (
    <div className="max-w-7xl mx-auto">
      <BookDetailItem book={book} />
    </div>
  );
}

export default BookDetailPage;
