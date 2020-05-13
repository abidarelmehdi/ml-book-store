import React from "react";
import Logo from "../core/Logo";
import NavLinks from "../core/NavLinks";
import ProfileDropDown from "../core/ProfileDropDown";
import { NavLink } from "react-router-dom";
import SearchBar from "./SearchBar";
export default function Navbar() {
  return (
    <nav className="bg-white shadow-sm">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-16">
          <div className="flex">
            <div className="flex-shrink-0 flex items-center text-indigo-500">
              <div className="block lg:hidden">
                <Logo size={12} />
              </div>
              <div className="hidden lg:block">
                <Logo size={12} />
              </div>
            </div>
            <div className="hidden sm:ml-6 sm:flex">
              <NavLinks />
            </div>
          </div>
          <div className="hidden sm:ml-6 sm:flex sm:items-center">
            {/* <!-- Profile dropdown --> */}
            <div className="flex-1 flex items-center justify-center px-2 lg:ml-6 lg:justify-end">
              <div className="max-w-2xl w-full lg:max-w-xs">
                <SearchBar />
              </div>
            </div>
            <NavLink
              to="/books/add"
              className="p-1 border-2 border-transparent text-gray-400 rounded-full hover:text-gray-500 focus:outline-none focus:text-gray-500 focus:bg-gray-100 transition duration-150 ease-in-out"
            >
              <svg
                fill="none"
                stroke="currentColor"
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth="2"
                viewBox="0 0 24 24"
                className="w-6 h-6"
              >
                <path d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-8l-4-4m0 0L8 8m4-4v12"></path>
              </svg>
            </NavLink>
            <ProfileDropDown />
          </div>
        </div>
      </div>
    </nav>
  );
}
