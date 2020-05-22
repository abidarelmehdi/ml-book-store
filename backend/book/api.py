from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from core.custom.pagination import StandardResultsSetPagination
from core.ai_models.content_based import CosineSimilarityModel
from book.models import Book, UserRatings
from book.serializers import BookSerializer, UserRatingsSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "authors__name"]


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


class UserRatedBookListView(ListAPIView):
    serializer_class = UserRatingsSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        current_user = self.request.user
        return current_user.user_ratings.all()


class BookRatings(APIView):
    def post(self, request):
        isbn = request.data.get("isbn")
        rate = int(request.data.get("rate"))
        rating, created = UserRatings.objects.update_or_create(
            book_id=isbn, user_id=request.user.id, defaults={"rate": rate},
        )
        serialized_rating = UserRatingsSerializer(rating).data
        return Response(serialized_rating)

    def get(self, request, isbn):
        rating = UserRatings.objects.filter(
            user=request.user, book_id=isbn
        ).first()
        rate = rating.rate if rating else -1
        return Response(rate)
