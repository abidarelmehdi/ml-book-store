import React, { useState } from "react";

export default function ProfileDropDown() {
  const [opened, setOpened] = useState(false);
  return (
    <div className="ml-3 relative">
      <button
        onClick={() => setOpened(!opened)}
        className="bg-gray-100 flex text-sm border-2 border-transparent rounded-full focus:outline-none focus:border-gray-300 transition duration-150 ease-in-out"
        id="user-menu"
        aria-label="User menu"
        aria-haspopup="true"
      >
        <svg
          fill="currentColor"
          viewBox="0 0 20 20"
          className="w-8 h-8 text-indigo-600 p-1"
        >
          <path
            fillRule="evenodd"
            d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z"
            clipRule="evenodd"
          ></path>
        </svg>
      </button>
      {/* <!--
            TODO
              Profile dropdown panel, show/hide based on dropdown state.

              Entering: "transition ease-out duration-200"
                From: "transform opacity-0 scale-95"
                To: "transform opacity-100 scale-100"
              Leaving: "transition ease-in duration-75"
                From: "transform opacity-100 scale-100"
                To: "transform opacity-0 scale-95"
            --> */}
      {opened && (
        <div className="origin-top-right absolute right-0 mt-2 w-48 rounded-md shadow-lg">
          <div className="py-1 rounded-md bg-white shadow-xs">
            <span className="block px-4 py-2 text-sm leading-5 text-gray-700 hover:bg-gray-100 focus:outline-none focus:bg-gray-100 transition duration-150 ease-in-out">
              Your Profile
            </span>
            <span className="block px-4 py-2 text-sm leading-5 text-gray-700 hover:bg-gray-100 focus:outline-none focus:bg-gray-100 transition duration-150 ease-in-out">
              Settings
            </span>
            <span className="block px-4 py-2 text-sm leading-5 text-gray-700 hover:bg-gray-100 focus:outline-none focus:bg-gray-100 transition duration-150 ease-in-out">
              Sign out
            </span>
          </div>
        </div>
      )}
    </div>
  );
}
