import logging
from typing import Any

from rest_framework.exceptions import ErrorDetail
from rest_framework.response import Response

logging.basicConfig(
    filename="error.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def success_response(data: Any, status: int) -> Response:
    return Response(
        data={
            "success": True,
            "data": data,
        },
        status=status,
        exception=False,
    )


def error_response(error: Exception, status: int) -> Response:
    error_detail = None

    if isinstance(error, ErrorDetail):
        error_detail = error.detail
    elif isinstance(error, str):
        logging.error(f"Error type: {error.__class__.__name__}, Message: {str(error)}")
    else:
        logging.error(f"Error type: {error.__class__.__name__}, Message: {str(error)}")
        error_detail = str(error)

    return Response(
        data={
            "success": False,
            "message": error_detail,
        },
        status=status,
        exception=True,
    )
