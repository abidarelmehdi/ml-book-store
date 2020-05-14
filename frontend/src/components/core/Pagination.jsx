import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { getParamFromUrl } from "../../common/functions";
import { withRouter } from "react-router-dom";

function Pagination({ data, history }) {
  const [pageNum, setPageNum] = useState(1);
  let currentUrl = history.location.search;
  currentUrl = currentUrl.includes("?") ? currentUrl + "&" : currentUrl + "?";

  useEffect(() => {
    setPageNum(getParamFromUrl("page"));
  }, [pageNum]);

  return (
    <nav className="mt-10 border-t border-gray-200 px-4 flex items-center justify-between sm:px-0">
      <div className="w-0 flex-1 flex">
        {data.previous && (
          <Link
            to={`${currentUrl}page=${data.page - 1}`}
            className="-mt-px border-t-2 border-transparent pt-4 pr-1 inline-flex items-center text-sm leading-5 font-medium text-gray-500 hover:text-gray-700 hover:border-gray-300 focus:outline-none focus:text-gray-700 focus:border-gray-400 transition ease-in-out duration-150"
          >
            Previous
          </Link>
        )}
      </div>
      <div className="hidden md:flex">
        <Link
          to={`${currentUrl}page=${data.page}`}
          className="-mt-px border-t-2 border-transparent pt-4 px-4 inline-flex items-center text-sm leading-5 font-medium text-gray-500 hover:text-gray-700 hover:border-gray-300 focus:outline-none focus:text-gray-700 focus:border-gray-400 transition ease-in-out duration-150"
        >
          {data.page}
        </Link>
      </div>
      <div className="w-0 flex-1 flex justify-end">
        {data.next && (
          <Link
            to={`${currentUrl}page=${data.page + 1}`}
            className="-mt-px border-t-2 border-transparent pt-4 pl-1 inline-flex items-center text-sm leading-5 font-medium text-gray-500 hover:text-gray-700 hover:border-gray-300 focus:outline-none focus:text-gray-700 focus:border-gray-400 transition ease-in-out duration-150"
          >
            Next
            <svg
              className="ml-3 h-5 w-5 text-gray-400"
              fill="currentColor"
              viewBox="0 0 20 20"
            >
              <path
                fillRule="evenodd"
                d="M12.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-2.293-2.293a1 1 0 010-1.414z"
                clipRule="evenodd"
              />
            </svg>
          </Link>
        )}
      </div>
    </nav>
  );
}

export default withRouter(Pagination);
