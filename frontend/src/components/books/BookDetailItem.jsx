import React from "react";
import BookStarsRating from "./BookStarsRating";
import BookStars from "./BookStars";
import { Link } from "react-router-dom";

export default function BookDetailItem({
  book,
  userRating,
  starClick,
  unrateClick,
}) {
  return (
    <>
      <div className="mt-20 w-full bg-white flex flex-col justify-between rounded shadow p-4">
        <div className="flex">
          <div className="-mt-10 flex-shrink-0">
            <img
              className="w-48 shadow-lg"
              src={book.thumbnail}
              alt={book.title}
            />
            <div className="mt-4 flex justify-center">
              <BookStarsRating
                userRating={userRating}
                starClick={starClick}
                unrateClick={unrateClick}
              />
            </div>
          </div>
          <div className="ml-4 flex-auto">
            <Link to={`/books/${book.id}`}>
              <h3 className="leading-6 text-2xl font-medium text-gray-800">
                {book.title}
              </h3>
            </Link>
            <div className="flex text-sm mt-6 text-gray-500">
              writed by
              <span className="ml-1 text-gray-700">
                {book.authors
                  .map((author) => {
                    return author.name;
                  })
                  .join(", ")}
              </span>
              <span className="mx-1">·</span>
              published by
              <span className="ml-1 text-gray-700">{book.publisher}</span>
            </div>
            <p className="text-sm mt-2 text-gray-500">
              <span className="text-gray-700">{book.pages}</span> Pages in
              <span className="ml-1 text-green-500">
                {book.categories.map((category) => category.label).join(", ")}
              </span>
            </p>
            <p className="text-sm mt-2 text-gray-500">ISBN: {book.isbn}</p>
            <div className="mt-6 flex items-center">
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
      </div>
    </>
  );
}
