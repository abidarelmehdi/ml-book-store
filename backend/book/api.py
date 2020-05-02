from rest_framework.viewsets import ModelViewSet
from core.custom.pagination import StandardResultsSetPagination
from book.models import Book
from book.serializers import BookSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = StandardResultsSetPagination
