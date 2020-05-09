from django.db import connection
import pandas as pd
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download("stopwords")


def compute_cosine_sim():
    """
        Compute All books cosine similarity score
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
    books_df = (
        df.copy().loc[df["raters"] >= rate_threshold].reset_index(drop=True)
    )

    # Define words to ignore during CountVectorizer
    stopwords_list = stopwords.words("english") + stopwords.words("french")

    # Define a count Vectorizer Object. Remove all english/french stop words
    # such as 'the', 'a', 'et'
    count = CountVectorizer(stop_words=stopwords_list)

    # Construct the required TF-IDF matrix by fitting and transforming the data
    count_matrix = count.fit_transform(books_df["features"])

    # Output the shape of tfidf_matrix
    count_matrix.shape

    cosine_sim = cosine_similarity(count_matrix, count_matrix)

    print("Good")
