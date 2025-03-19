from typing import Any

from core.responses import error_response, success_response
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response

from apps.plan.models import Book, Category

from .serializers import BookSerializer, CategorySerializer
from .services import BookService


class CategoryAPIView(generics.ListCreateAPIView[Category]):
    serializer_class = CategorySerializer

    def get_queryset(self):
        super().get_queryset()
        categories = Category.objects.all()
        return categories

    def list(self, request: Request) -> Response:
        super().list(request)
        c = Category.objects.all()
        srz = CategorySerializer(c, many=True)
        return success_response(data=srz.data, status=status.HTTP_200_OK)

    def create(self, request: Request) -> Response:
        super().create(request)
        srz = CategorySerializer(data=request.data)
        if srz.is_valid():
            srz.save()
            return success_response(data=srz.data, status=status.HTTP_201_CREATED)
        else:
            print(srz)
            return error_response(error=srz.errors, status=status.HTTP_400_BAD_REQUEST)


class BookAPIView(generics.ListCreateAPIView[Book]):
    serializer_class = BookSerializer

    def list(self, request: Request) -> Response:
        super().list(request)
        c = Book.objects.all()
        srz = BookSerializer(c, many=True)
        return success_response(data=srz.data, status=status.HTTP_200_OK)

    def create(self, request: Request) -> Response:
        super().create(request)
        srz = BookSerializer(data=request.data)
        if srz.is_valid():
            srz.save()
            return success_response(data=srz.data, status=status.HTTP_201_CREATED)
        else:
            return error_response(error=srz.errors, status=status.HTTP_400_BAD_REQUEST)


class BookEditAPIView(generics.RetrieveUpdateDestroyAPIView[Book]):
    serializer_class = BookSerializer

    def get_object(self) -> str:
        pid = self.kwargs["pid"]
        return pid

    def retrieve(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        super().retrieve(request, *args, **kwargs)
        pid = self.get_object()
        book_object = BookService.get_book(pid)
        srz = BookSerializer(book_object)
        return success_response(data=srz.data, status=status.HTTP_200_OK)

    def patch(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        super().patch(request, *args, **kwargs)
        data = request.data
        pid = self.get_object()
        book_object = BookService.get_book(pid)
        srz = BookSerializer(
            book_object,
            data,
            partial=True,
        )
        if srz.is_valid():
            srz.save()
            return success_response(data=srz.data, status=status.HTTP_200_OK)
        else:
            return error_response(data=srz.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        super().destroy(request, *args, **kwargs)
        pid = self.get_object()
        book_object = BookService.get_book(pid)
        book_object.delete()
        return success_response(data=None, status=status.HTTP_204_NO_CONTENT)
