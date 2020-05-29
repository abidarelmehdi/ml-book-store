import React, { useEffect } from "react";
import { connect } from "react-redux";
import * as bookActions from "../../redux/actions/bookActions";
import * as userPrefBooksActions from "../../redux/actions/userPrefBooksActions";
import BooksList from "../books/BooksList";
import SuggestedBooks from "../books/SuggestedBooks";

function Home({ books, loadBooks, userPrefBooks, loadUserPrefBooks, history }) {
  useEffect(() => {
    const queryString = history.location.search;
    loadBooks(queryString);
    userPrefBooks.length === 0 && loadUserPrefBooks();
  }, [
    loadBooks,
    userPrefBooks.length,
    loadUserPrefBooks,
    history.location.search,
  ]);

  return (
    <>
      <div className="mt-10">
        <SuggestedBooks
          books={userPrefBooks}
          title={"Based on what you rated"}
        />
      </div>
      <BooksList books={books} />
    </>
  );
}

function mapStateToProps(state) {
  return {
    loading: state.apiStatus > 0,
    books: state.books,
    userPrefBooks: state.userPrefBooks,
  };
}

const mapDispatchToProps = {
  loadBooks: bookActions.loadBooks,
  loadUserPrefBooks: userPrefBooksActions.loadUserPrefBooks,
};
export default connect(mapStateToProps, mapDispatchToProps)(Home);
