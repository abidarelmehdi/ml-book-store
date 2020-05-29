import nltk
import pandas as pd
import numpy as np
from nltk.corpus import stopwords
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

from django.db import connection
from django_redis import get_redis_connection


class UserPreferencesModel(object):
    """
        Content-Based model based on user's preferences
        by calculatig the dot product of user's ratings and books categories
    """

    def __init__(self, database="ai", train=False):
        #     self.connection = get_redis_connection(database)

        #     # if train flag is True, the model will be trained during intanciation
        #     if train:
        #         self.train(build=True)

        # def build_dataframe(self):
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

    # def train(self, build=False):
    #     pass

    # def predict(self, userInputs):
    def predict(self, userInputs):
        books_pivot = pd.get_dummies(
            self.books_df["categorie"].groupby("book_id").max()
        )
        userInputs = pd.DataFrame(userInputs).set_index("book_id")
        userBooks = books_pivot[books_pivot.index.isin(userInputs.index)]
        userProfile = userBooks.transpose().dot(userInputs["rate"])
        recommendationTable_df = ((books_pivot * userProfile).sum(axis=1)) / (
            userProfile.sum()
        )
        recommendationTable_df = recommendationTable_df.sort_values(
            ascending=False
        )
        recommended_books = self.books_df[
            self.books_df.index.isin(recommendationTable_df.head(10).index)
        ]
        return recommended_books.index.to_list()
