import React, { useState, useEffect } from "react";
import { getBookbyId, rateBook, unrateBook } from "../../api/bookApi";
import BookDetailItem from "../books/BookDetailItem";
import SuggestedBooks from "../books/SuggestedBooks";
import { getCoSinSimilarBooks, UserBookRating } from "../../api/bookApi";

function BookDetailPage({ match }) {
  const [book, setBook] = useState({
    authors: [],
    categories: [],
  });
  const [similarBooks, setSimilarBooks] = useState([]);
  const [userRating, setUserRating] = useState(0);

  useEffect(() => {
    getBookbyId(match.params.id).then((_book) => setBook(_book.data));

    getCoSinSimilarBooks(book.isbn).then((_books) => {
      setSimilarBooks(_books.data);
    });

    UserBookRating(book.isbn).then((res) => setUserRating(res.data));
  }, [book.isbn, book.raters, match.params.id]);

  function handleStarClick(rate) {
    rateBook(book.isbn, rate).then((_book) => setBook(_book.data));
  }

  function handleUnrateClick() {
    unrateBook(book.isbn).then((_book) => setBook(_book.data));
  }

  return (
    <div className="max-w-7xl mx-auto">
      <BookDetailItem
        book={book}
        userRating={userRating}
        starClick={handleStarClick}
        unrateClick={handleUnrateClick}
      />
      <div className="mt-10">
        <SuggestedBooks books={similarBooks} />
      </div>
    </div>
  );
}

export default BookDetailPage;
