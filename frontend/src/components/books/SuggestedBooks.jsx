import React from "react";
import SmallBookItem from "./SmallBookItem";

export default function SuggestedBooks({ books, title = "Similar Books" }) {
  return (
    <>
      <h4 className="text-xl font-medium text-gray-600">{title}</h4>
      <div className="rounded shadow bg-white mt-6 w-full flex overflow-x-auto">
        {books.map((book) => (
          <div key={book.id} className="mr-4">
            <SmallBookItem book={book} />
          </div>
        ))}
      </div>
    </>
  );
}
