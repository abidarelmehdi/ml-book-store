import React from "react";
import BookItem from "./BookItem";
import Pagination from "../core/Pagination";

export default function BooksList({ books }) {
  return (
    <>
      <div className="mt-28 grid gap-8 row-gap-16 sm:grid-cols-2 sm:grid-cols-2 lg:grid-cols-3">
        {books.results.map((book) => (
          <BookItem key={book.id} book={book} />
        ))}
      </div>
      <Pagination data={books} />
    </>
  );
}
