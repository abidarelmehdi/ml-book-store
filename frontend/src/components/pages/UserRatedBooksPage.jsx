import React, { useEffect } from "react";
import { connect } from "react-redux";
import * as ratedBooksActions from "../../redux/actions/ratedBooksActions";
import RatedBooksList from "../books/RatedBooksList";

function UserRatedBooksPage({ ratedBooks, loadRatedBooks }) {
  useEffect(() => {
    loadRatedBooks();
  }, [loadRatedBooks]);
  return <RatedBooksList ratedBooks={ratedBooks} />;
}

function mapStateToProps(state) {
  return {
    loading: state.apiStatus > 0,
    ratedBooks: state.ratedBooks,
  };
}

const mapDispatchToProps = {
  loadRatedBooks: ratedBooksActions.loadRatedBooks,
};
export default connect(mapStateToProps, mapDispatchToProps)(UserRatedBooksPage);
