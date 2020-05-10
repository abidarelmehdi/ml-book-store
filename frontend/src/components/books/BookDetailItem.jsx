import React from "react";
import BookStarsRating from "./BookStarsRating";
import BookStars from "./BookStars";
import { Link } from "react-router-dom";
export default function BookItem({ book }) {
  return (
    <div className="mt-20 w-full bg-white flex flex-col justify-between rounded shadow p-4">
      <div className="flex">
        <div className="-mt-10 flex-shrink-0">
          <img
            className="w-48 shadow-lg"
            src={book.thumbnail}
            alt={book.title}
          />
          <div className="mt-4 flex justify-center">
            <BookStarsRating />
          </div>
        </div>
        <div className="ml-4 flex-auto">
          <Link to={`books/${book.id}`}>
            <h3 className="leading-6 text-2xl font-medium text-gray-800">
              {book.title}
            </h3>
          </Link>
          <p className="text-sm mt-4 text-gray-500">
            Writed by
            <span className="ml-1">
              {book.authors
                .map((author) => {
                  return author.name;
                })
                .join(", ")}
            </span>
          </p>
          <div className="mt-2 flex items-center">
            <BookStars rating={book.avg_ratings} />

            <p className="ml-2 text-sm font-light text-gray-400">
              {book.raters} voters
            </p>
          </div>
          <div className="mt-8">
            <h4 className="leading-6 text-lg text-gray-700">Description</h4>
            <p className="text-sm mt-3 leading-5 font-light text-gray-500">
              {book.description}
            </p>
          </div>
        </div>
      </div>
      <div className="mt-4 border-t border-gray-100">
        <p className="mt-3 text-xs leading-5 text-gray-600">
          in
          <span className="ml-1">
            {book.categories.map((category) => category.label).join(", ")}
          </span>
        </p>
      </div>
    </div>
  );
}
