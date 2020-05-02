import React from "react";
import BookItem from "./BookItem";

export default function BooksList({ books }) {
  return (
    <div className="mt-12 grid gap-8 row-gap-16 sm:grid-cols-2 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-5">
      {books.map((book) => (
        <BookItem key={book.id} book={book} />
      ))}
    </div>
  );
}
