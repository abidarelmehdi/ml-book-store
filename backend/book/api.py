from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from core.custom.pagination import StandardResultsSetPagination
from book.models import Book, UserRatings
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


class BookRatings(APIView):
    def post(self, request):
        isbn = request.data.get("isbn")
        rate = int(request.data.get("rate"))
        obj, created = UserRatings.objects.update_or_create(
            book_id=isbn, user_id=request.user.id, defaults={"rate": rate},
        )
        return Response(obj)

    def get(self, request, isbn):
        rating = UserRatings.objects.filter(
            user=request.user, book_id=isbn
        ).first()
        rate = rating.rate if rating else -1
        return Response(rate)
