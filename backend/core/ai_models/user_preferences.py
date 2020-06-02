import os
import pandas as pd
import numpy as np
from django.db import connection


class UserPreferencesModel(object):
    """
        Content-Based model based on user's preferences
        by computing the weighted average for each book based on the weight of 
        each category for this user.
    """

    def __init__(self, train=False):
        dir_path = os.path.join(os.path.dirname(__file__), "models")
        self.books_path = os.path.join(dir_path, "books_categories.parquet")
        self.users_path = os.path.join(dir_path, "users_categories.parquet")
        if train:
            self.train(build=True)

    def build_dataframe(self):
        """
            Fill Dataframe from Django main database with a SQL query
        """

        # Build Dataframe from database using Django connection
        self.books_df = pd.read_sql(
            """
                SELECT
                    isbn,
                    label as category
                FROM
                    book_book
                    JOIN book_book_categories
                    ON book_book_categories.book_id = book_book.id
                    JOIN category_category
                    ON category_category.id = book_book_categories.category_id
            """,
            connection,
        )

        self.ratings_df = pd.read_sql(
            """
                SELECT
                    user_id,
                    book_id as isbn,
                    rate
                FROM
                    book_userratings
            """,
            connection,
        )

        # Flag that idicates that the Dataframe is filled with data
        self.is_filled = True

    def train(self, build=False):
        """
            Train the model to generate the top 10 similar books
            based on user profile
        """

        # if build flag is true, Dataframe will be built before train the model
        if build:
            self.build_dataframe()

        # Check Dataframe state before training the model
        if not self.is_filled:
            raise Exception(
                "You cannot train the model before building the Dataframe"
            )

        books_categories_pivot = (
            pd.get_dummies(self.books_df.set_index("isbn")["category"])
            .groupby("isbn")
            .sum()
        )
        users_categories = pd.merge(
            self.ratings_df,
            self.books_df[["isbn", "category"]],
            on="isbn",
            how="left",
        )
        categories_not_rated = self.books_df[
            ~self.books_df["category"].isin(users_categories["category"])
        ]["category"]
        categories_not_rated = dict.fromkeys(categories_not_rated, 0)
        users_categories_pivot = users_categories.pivot_table(
            index="user_id",
            columns="category",
            values="rate",
            fill_value=0,
            aggfunc=np.sum,
        ).assign(**categories_not_rated)

        # Savingk Books/Categories datatframe
        books_categories_pivot.to_parquet(self.books_path)

        # Saving Users/Categories datatframe
        users_categories_pivot.to_parquet(self.users_path)

    def predict(self, user_inputs, nbr_books=10):
        user_id, user_rated_books = user_inputs
        try:
            books_categories_pivot = pd.read_parquet(self.books_path)
            users_categories_pivot = pd.read_parquet(self.users_path)
        except Exception:
            raise Exception("Model not trained yet !")

        books_categories_pivot = books_categories_pivot[
            ~books_categories_pivot.index.isin(user_rated_books)
        ]
        user_profile = users_categories_pivot.loc[user_id]

        user_books = round(
            (books_categories_pivot * user_profile).sum(axis=1)
            / user_profile.sum(),
            3,
        )

        top_n_books = (
            user_books.sort_values(ascending=False).head(nbr_books).index
        )

        return top_n_books.to_list()
