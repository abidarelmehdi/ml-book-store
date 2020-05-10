import nltk
import pandas as pd
from nltk.corpus import stopwords
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

from django.db import connection
from django_redis import get_redis_connection


class CosineSimilarityModel(object):
    """
        Content-Based model based on cosine similarity score
        of all books
    """

    def __init__(self, database="ai", train=False):
        self.connection = get_redis_connection(database)

        # if train flag is True, the model will be trained during intanciation
        if train:
            self.train(build=True)

    def build_dataframe(self):
        """
            Fill Dataframe from Django main database with a SQL query
        """
        # SQL query to retrieve data directly from database
        query = """
            SELECT bb.isbn,
                bb.title,
                    bb.raters,
                    concat(
                        string_agg(DISTINCT cc.label, ' '), ' ',
                        string_agg(DISTINCT initcap(aa.name), ' '), ' ',
                        bb.publisher
                    ) as features

            FROM ((((book_book bb
                JOIN book_book_categories bc ON ((bb.id = bc.book_id)))
                JOIN category_category cc ON ((bc.category_id = cc.id)))
                JOIN book_book_authors ba ON ((bb.id = ba.book_id)))
                JOIN author_author aa ON ((ba.author_id = aa.id)))
            GROUP BY bb.isbn, bb.title, bb.publisher, bb.pages,
                        bb.raters, bb.avg_ratings
        """

        # Build Dataframe from database using Django connection
        df = pd.read_sql(query, connection)

        # Compute a threshold based on 70th quantile
        rate_threshold = df["raters"].quantile(0.70)

        # Based filter based in rate threshold
        self.df = (
            df.copy().loc[df["raters"] >= rate_threshold].reset_index(drop=True)
        )

        # Flag that idicates that the Dataframe is filled with data
        self.is_filled = True

    def train(self, build=False):
        """
            Train the model to generate the top 10 cosine simarily score
            for all books
        """

        # StopWords dataset from nltk library ("and", "et", "ou", "the", "le")
        nltk.download("stopwords")

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

        cosine_sim = cosine_similarity(count_matrix, count_matrix)

        # ******* Store in Cosine Similarity Matrix Redis *******

        # Clear Databse before storing data
        self.connection.flushdb()

        # Store each book with his similar books
        # each book identified by his ISBN
        for idx, row in self.df.iterrows():
            similar_indices = cosine_sim[idx].argsort()[:-12:-1]
            similar_items = {
                self.df["isbn"][i]: cosine_sim[idx][i]
                for i in similar_indices[1:]
            }

            self.connection.hmset(row["isbn"], similar_items)

    def predict(self, isbn):
        return self.connection.hgetall(isbn)
