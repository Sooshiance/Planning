from rest_framework import serializers

from apps.plan.models import Book, Category


class CategorySerializer(serializers.ModelSerializer[Category]):
    class Meta:
        model = Category
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer[Book]):
    class Meta:
        model = Book
        fields = "__all__"
