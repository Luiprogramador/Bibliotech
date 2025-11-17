from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from catalog.models import Book
from api.serializers import BookSerializer
from rest_framework import filters

class BookViewSet(ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author__name', 'publisher__name', 'genre', 'isbn_number']
# Create your views here.
