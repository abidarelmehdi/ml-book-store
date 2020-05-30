import nltk
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import pyarrow as pa
from django.db import connection


class UserPreferencesModel(object):
    """
        Content-Based model based on user's preferences
        by calculatig the dot product of user's ratings and books categories
    """

    def __init__(self, train=False):
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
                    isbn as book_id,
                    label as categorie
                FROM
                    book_book
                    JOIN book_book_categories
                    ON book_book_categories.book_id = book_book.id
                    JOIN category_category
                    ON category_category.id = book_book_categories.category_id
            """,
            connection,
            index_col="book_id",
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

        pd.get_dummies(
            self.books_df["categorie"].groupby("book_id").max()
        ).to_parquet("model.prq")

    def predict(self, userInputs):
        books_pivot = pd.read_parquet("model.prq")
        userInputs = pd.DataFrame(userInputs).set_index("book_id")
        userBooks = books_pivot[books_pivot.index.isin(userInputs.index)]
        userProfile = userBooks.transpose().dot(userInputs["rate"])
        recommendationTable_df = ((books_pivot * userProfile).sum(axis=1)) / (
            userProfile.sum()
        )
        recommended_books = (
            recommendationTable_df.sort_values(ascending=False).head(10).index
        )
        return recommended_books.to_list()
