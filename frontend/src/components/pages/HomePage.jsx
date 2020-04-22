import React, { useEffect } from "react";

export default function Home({ setTitle }) {
  useEffect(() => {
    setTitle("Home Page");
  });
  return <></>;
}
