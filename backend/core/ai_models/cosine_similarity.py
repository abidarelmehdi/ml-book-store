import nltk
import os
from django.db import connection

import pandas as pd
from nltk.corpus import stopwords
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer


class CosineSimilarityModel(object):
    """
        Content-Based model based on cosine similarity score
        of all books
    """

    def __init__(self, train=False):
        dir_path = os.path.join(os.path.dirname(__file__), "models")
        self.books_path = os.path.join(
            dir_path, "books_cosine_similarity.parquet"
        )

        # if train flag is True, the model will be trained during intanciation
        if train:
            self.train(build=True)

    def build_dataframe(self):
        """
            Fill Dataframe from Django main database with a SQL query
        """
        # SQL query to retrieve data directly from database
        books_df = pd.read_sql(
            """
                SELECT
                    b.isbn,
                    title,
                    pages,
                    c.label category,
                    a.name author,
                    publisher
                FROM
                    book_book b
                    JOIN book_book_categories bc ON bc.book_id = b.id
                    JOIN category_category c ON c.id = bc.category_id
                    JOIN book_book_authors ba ON ba.book_id = b.id
                    JOIN author_author a ON a.id = ba.author_id
            """,
            connection,
        )
        # Features considered in content filtering
        features = ["isbn", "publisher", "category", "author"]

        # Join all the features in one column to build a bag of words
        books_df = (
            books_df[features]
            .groupby("isbn")
            .agg(lambda cell_val: " ".join(set(cell_val)))
        )
        books_df["features"] = books_df[features[1:]].apply(
            lambda row: " ".join(row.fillna("")), axis=1
        )

        self.df = books_df
        # Flag that idicates that the Dataframe is filled with data
        self.is_filled = True

    def train(self, build=False):
        """
            Train the model to generate the cosine simarily score
            for all books
        """

        # StopWords dataset from nltk library ("and", "et", "ou", "the", "le")
        nltk.download("stopwords", quiet=True)

        # if build flag is true, Dataframe will be built before train the model
        if build:
            self.build_dataframe()

        # Check Dataframe state before training the model
        if not self.is_filled:
            raise Exception(
                "You cannot train the model before building the Dataframe"
            )

        # Define words to ignore during CountVectorizer
        # such as 'the', 'a', 'et'
        stopwords_list = stopwords.words("english") + stopwords.words("french")

        # Define a count Vectorizer Object
        count = CountVectorizer(stop_words=stopwords_list)

        # Construct the required count matrix
        count_matrix = count.fit_transform(self.df["features"])

        cosine_matrix = cosine_similarity(count_matrix, count_matrix)

        # ******* Store the Cosine Similarity Matrix *******

        pd.DataFrame(
            cosine_matrix, columns=self.df.index, index=self.df.index
        ).to_parquet(self.books_path)

    def predict(self, isbn, nbr_books=10):
        books_cos_df = pd.read_parquet(self.books_path)
        recommended_books = books_cos_df.loc[isbn].sort_values(ascending=False)[
            1 : nbr_books + 1
        ]
        return recommended_books.index.to_list()
