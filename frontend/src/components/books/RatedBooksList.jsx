import React from "react";
import RatedBookItem from "./RatedBookItem";
import Pagination from "../core/Pagination";

export default function RatedBooksList({ ratedBooks }) {
  return (
    <div className="max-w-7xl mx-auto">
      <div className="mt-28 grid gap-8 row-gap-16 sm:grid-cols-2 sm:grid-cols-2 lg:grid-cols-3">
        {ratedBooks.results.map((userRating) => (
          <RatedBookItem
            key={userRating.book.id}
            book={userRating.book}
            rate={userRating.rate}
          />
        ))}
      </div>
      <Pagination data={ratedBooks} />
    </div>
  );
}
