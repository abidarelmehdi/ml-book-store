from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from core.custom.pagination import StandardResultsSetPagination
from book.models import Book
from book.serializers import BookSerializer
from core.ai_models.content_based import CosineSimilarityModel


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = StandardResultsSetPagination


class RecommendedBooksListView(ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        # Initiate new instance of cosine similarity model
        model = CosineSimilarityModel()

        # Get ISBN of predicted books
        isbn_recommended_books = model.predict(self.kwargs.get("isbn"))

        # Get all books with those ISBNs
        recommended_books = Book.objects.filter(
            isbn__in=isbn_recommended_books.keys()
        )

        return recommended_books
