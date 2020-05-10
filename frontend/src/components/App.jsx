import React, { useState } from "react";
import { Route, Switch } from "react-router-dom";
import Navbar from "./core/Navbar";
import HomePage from "./pages/HomePage";
import BookManage from "./pages/BookManage";
import BookDetailPage from "./pages/BookDetailPage";
import Login from "./pages/Login";

export default function App() {
  const [title, setTitle] = useState("");
  return (
    <>
      <Navbar />
      <div className="py-10">
        {title && (
          <header>
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
              <h1 className="text-3xl font-bold leading-tight text-gray-900">
                {title}
              </h1>
            </div>
          </header>
        )}
        <main>
          <div className="mx-auto sm:px-6 lg:px-8">
            <Switch>
              <Route
                exact
                path="/"
                render={(props) => <HomePage {...props} setTitle={setTitle} />}
              />
              <Route
                exact
                path="/books/add"
                render={(props) => (
                  <BookManage {...props} setTitle={setTitle} />
                )}
              />
              <Route exact path="/books/add" component={BookManage} />
              <Route exact path="/books/:id" component={BookDetailPage} />
              <Route exact path="/login" component={Login} />
            </Switch>
          </div>
        </main>
      </div>
    </>
  );
}
