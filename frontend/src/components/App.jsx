import React from "react";
import { Route, Switch } from "react-router-dom";
import Navbar from "./core/Navbar";
import HomePage from "./pages/HomePage";
import BookManage from "./pages/BookManage";
import BookDetailPage from "./pages/BookDetailPage";
import Login from "./pages/Login";
import PrivateRoute from "./core/PrivateRoute";

export default function App() {
  return (
    <>
      <Navbar />
      <div className="py-10">
        <main>
          <div className="mx-auto sm:px-6 lg:px-8">
            <Switch>
              <PrivateRoute exact path="/books/add" component={BookManage} />
              <PrivateRoute exact path="/books" component={HomePage} />
              <PrivateRoute
                exact
                path="/books/:id"
                component={BookDetailPage}
              />
              <Route exact path="/login" component={Login} />
              <PrivateRoute exact path="/" component={HomePage} />
            </Switch>
          </div>
        </main>
      </div>
    </>
  );
}
