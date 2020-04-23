import React from "react";
import BookItem from "./BookItem";

export default function BooksList({ books }) {
  return (
    <div className="mt-12 grid gap-5 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5">
      {books.map((book) => (
        <BookItem key={book.id} book={book} />
      ))}
    </div>
  );
}
