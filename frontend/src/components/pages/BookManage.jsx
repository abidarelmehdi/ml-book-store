import React, { useEffect } from "react";

export default function BookManage({ setTitle }) {
  useEffect(() => {
    setTitle("Add new book");
  });
  return <div className="px-4 py-8 sm:px-0">Manage</div>;
}
