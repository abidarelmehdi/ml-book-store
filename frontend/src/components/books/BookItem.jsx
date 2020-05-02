import React from "react";
import Truncate from "react-truncate";

export default function BookItem({ book }) {
  return (
    <div className="bg-white flex flex-col justify-between rounded shadow p-4">
      <div className="flex">
        <div className="-mt-10 flex-shrink-0">
          <img
            className="w-36 shadow-lg"
            src={book.thumbnail}
            alt={book.title}
          />
        </div>
        <div className="ml-4 flex-auto">
          <h3 className="leading-6 text-gray-800">{book.title}</h3>
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
            <div className="flex">
              <span className="text-yellow-300">
                <svg
                  className="w-5 h-5"
                  fill="currentColor"
                  viewBox="0 0 20 20"
                >
                  <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path>
                </svg>
              </span>
              <span className="text-yellow-300">
                <svg
                  className="w-5 h-5"
                  fill="currentColor"
                  viewBox="0 0 20 20"
                >
                  <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path>
                </svg>
              </span>
              <span className="text-yellow-300">
                <svg
                  className="w-5 h-5"
                  fill="currentColor"
                  viewBox="0 0 20 20"
                >
                  <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path>
                </svg>
              </span>
              <span className="text-yellow-300">
                <svg
                  className="w-5 h-5"
                  fill="currentColor"
                  viewBox="0 0 20 20"
                >
                  <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path>
                </svg>
              </span>
              <span className="text-yellow-300">
                <svg
                  className="w-5 h-5"
                  fill="currentColor"
                  viewBox="0 0 20 20"
                >
                  <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path>
                </svg>
              </span>
            </div>
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
        <p className="mt-3 text-xs leading-5 text-gray-600">
          in
          <span className="ml-1">
            {book.categories.map((category) => category.label).join(", ")}
          </span>
        </p>
      </div>
    </div>
    // <div
    //   dir={book.language === "ar" ? "rtl" : ""}
    //   className="bg-white flex flex-col rounded-lg shadow-lg overflow-hidden"
    // >
    //   <div className="flex-shrink-0">
    //     <img
    //       className="h-64 w-full object-cover object-top"
    //       src={book.thumbnail}
    //       alt={book.title}
    //     />
    //   </div>
    //   <div className="flex-1 bg-white p-6 flex flex-col justify-between">
    //     <div className="flex-1">
    //       <p className="text-xs leading-5 font-medium text-indigo-400">
    //         {book.categories.map((category) => (
    //           <span key={category.id} className="hover:underline">
    //             {category.label}
    //           </span>
    //         ))}
    //       </p>
    //       <h3 className="block mt-2 text-lg leading-6 font-semibold text-gray-900">
    //         {book.title}
    //       </h3>
    //     </div>
    //     {book.authors.map((author) => (
    //       <div key={author.id} className="mt-6 flex items-center">
    //         <div className={book.language === "ar" ? "mr-3" : "ml-3"}>
    //           <p className="text-sm leading-5 font-medium text-gray-900">
    //             <span className="hover:underline">{author.name}</span>
    //           </p>
    //         </div>
    //       </div>
    //     ))}
    //   </div>
    // </div>
  );
}
