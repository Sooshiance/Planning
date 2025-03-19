import logging

from django.utils.deprecation import MiddlewareMixin
from rest_framework.exceptions import APIException
from rest_framework.request import Request
from rest_framework.response import Response

logger = logging.getLogger("error_logger")


class JsonErrorLoggingMiddleware(MiddlewareMixin):
    def process_exception(self, request: Request, exception: APIException) -> None:
        """Log unhandled exceptions (500 errors)"""
        extra = {
            "status": 500,
            "method": request.method,
            "path": request.path,
            "user": str(request.user) if request.user.is_authenticated else "Anonymous",
            "user_agent": request.META.get("HTTP_USER_AGENT", ""),
            "ip": request.META.get("REMOTE_ADDR"),
            "exception_type": type(exception).__name__,
            "exception_message": str(exception),
        }
        logger.error(
            "Server error occurred",
            exc_info=exception,
            extra=extra,
        )
        return None

    def process_response(self, request: Request, response: Response) -> Response:
        """Log 4xx client errors and any 5xx errors not from exceptions"""
        if 400 <= response.status_code < 500:
            self._log_client_error(request, response)
        elif response.status_code >= 500 and not getattr(
            request, "exception_logged", False
        ):
            self._log_server_error(request, response)
        return response

    def _log_client_error(self, request: Request, response: Response) -> None:
        extra = {
            "status": response.status_code,
            "method": request.method,
            "path": request.path,
            "user": str(request.user) if request.user.is_authenticated else "Anonymous",
            "user_agent": request.META.get("HTTP_USER_AGENT", ""),
            "ip": request.META.get("REMOTE_ADDR"),
        }
        try:
            extra["response_content"] = response.content.decode("utf-8")[:500]
        except UnicodeDecodeError:
            extra["response_content"] = "[Unable to decode content]"

        logger.error(
            "Client error occurred",
            extra=extra,
        )

    def _log_server_error(self, request: Request, response: Response) -> None:
        extra = {
            "status": response.status_code,
            "method": request.method,
            "path": request.path,
            "user": str(request.user) if request.user.is_authenticated else "Anonymous",
            "user_agent": request.META.get("HTTP_USER_AGENT", ""),
            "ip": request.META.get("REMOTE_ADDR"),
        }
        try:
            extra["response_content"] = response.content.decode("utf-8")[:500]
        except UnicodeDecodeError:
            extra["response_content"] = "[Unable to decode content]"

        logger.error(
            "Server error occurred",
            extra=extra,
        )
