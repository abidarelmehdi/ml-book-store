import React from "react";
import { Link } from "react-router-dom";

export default function SmallBookItem({ book }) {
  return (
    <div className="w-48 text-center rounded p-4">
      <div>
        <img
          className="w-24 shadow-lg mx-auto"
          src={book.thumbnail}
          alt={book.title}
        />
      </div>
      <div className="mt-4">
        <Link to={`/books/${book.id}`}>
          <h3 className="text-sm font-medium leading-5 text-blue-600">
            {book.title}
          </h3>
        </Link>
        <p className="text-sm mt-2 leading-4 text-gray-500">
          by
          <span className="ml-1">
            {book.authors
              .map((author) => {
                return author.name;
              })
              .join(", ")}
          </span>
        </p>
      </div>
    </div>
  );
}
