import React from "react";
import Truncate from "react-truncate";
import BookStars from "./BookStars";
import { Link } from "react-router-dom";
export default function BookItem({ book, rate }) {
  return (
    <div className="w-full bg-white flex flex-col justify-between rounded shadow p-4">
      <div className="flex">
        <div className="-mt-10 flex-shrink-0">
          <img
            className="w-36 shadow-lg"
            src={book.thumbnail}
            alt={book.title}
          />
        </div>
        <div className="ml-4 flex-auto">
          <Link to={`/books/${book.id}`}>
            <h3 className="leading-6 text-gray-800">{book.title}</h3>
          </Link>
          <p className="text-sm leading-5 text-gray-500">
            by
            <span className="ml-1">
              {book.authors
                .map((author) => {
                  return author.name;
                })
                .join(", ")}
            </span>
          </p>
          <div className="mt-3 flex justify-between items-center">
            <BookStars rating={book.avg_ratings} />
            <p className="text-sm font-light text-gray-400">
              {book.raters} voters
            </p>
          </div>
          <p className="text-sm mt-3 leading-5 font-light text-gray-500">
            <Truncate lines={4}>{book.description}</Truncate>
          </p>
        </div>
      </div>
      <div className="mt-4 border-t border-gray-100">
        <div className="mt-3 flex items-center justify-between">
          <p className="text-xs leading-5 text-gray-600">
            in
            <span className="ml-1">
              {book.categories.map((category) => category.label).join(", ")}
            </span>
          </p>
          <div>
            <BookStars rating={rate} />
          </div>
        </div>
      </div>
    </div>
  );
}
