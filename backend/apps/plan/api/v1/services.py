from apps.plan.models import Book


class BookService:
    @staticmethod
    def get_book(pid: str) -> Book | Exception:
        try:
            book_object = Book.objects.get(pid=pid)
            return book_object
        except Book.DoesNotExist as e:
            return e
