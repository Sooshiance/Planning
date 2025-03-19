from django.urls import path

from .views import BookAPIView, BookEditAPIView, CategoryAPIView

urlpatterns = [
    path("category/", CategoryAPIView.as_view(), name=""),
    path("book/", BookAPIView.as_view(), name="books"),
    path("book/<str:pid>/", BookEditAPIView.as_view(), name="book"),
]
