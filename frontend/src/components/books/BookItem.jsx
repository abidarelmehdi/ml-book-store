import React from "react";

export default function BookItem({ book }) {
  return (
    <div
      dir={book.language === "ar" ? "rtl" : ""}
      className="bg-white flex flex-col rounded-lg shadow-lg overflow-hidden"
    >
      <div className="flex-shrink-0">
        <img
          className="h-56 w-full object-contain"
          src={book.thumbnail}
          alt={book.title}
        />
      </div>
      <div className="flex-1 bg-white p-6 flex flex-col justify-between">
        <div className="flex-1">
          <p className="text-sm leading-5 font-medium text-indigo-600">
            {book.categories.map((category) => (
              <span key={category.id} className="hover:underline">
                {category.label}
              </span>
            ))}
          </p>
          <h3 className="block mt-2 text-xl leading-7 font-semibold text-gray-900">
            {book.title}
          </h3>
        </div>
        {book.authors.map((author) => (
          <div key={author.id} className="mt-6 flex items-center">
            <div className="flex-shrink-0">
              <img
                className="h-10 w-10 rounded-full"
                src={author.picture}
                alt={author.first_name + " " + author.last_name}
              />
            </div>
            <div className={book.language === "ar" ? "mr-3" : "ml-3"}>
              <p className="text-sm leading-5 font-medium text-gray-900">
                <span className="hover:underline">
                  {author.first_name + " " + author.last_name}
                </span>
              </p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
