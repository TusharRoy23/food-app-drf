from rest_framework import status
from rest_framework.exceptions import (
    APIException,
    MethodNotAllowed,
    NotFound,
    ValidationError,
)
from rest_framework.response import Response


class CustomBaseException(Exception):
    """
    This class can be handled by exception handler
    """

    code = None
    error_code = None
    errors = None
    message = None
    context = None
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

    def __init__(
        self,
        message="",
        context=None,
        errors=None,
        code=None,
        error_code=None,
        *args,
        **kwargs
    ):
        self.code = code
        self.error_code = error_code
        self.message = message
        self.errors = errors
        self.context = context

        if kwargs:
            self.context.update(kwargs)

        if self.context and self.message:
            self.message = self.message.format(**self.context)

    def __str__(self):
        return str(self.message)


class RequestTimeoutException(CustomBaseException):
    errors = {
        "error_code": "REQUEST_TIMEOUT",
        "message": "Request timeout",
    }
    status_code = status.HTTP_408_REQUEST_TIMEOUT


class TimeOutException(CustomBaseException):
    code = "REQUEST_TIMED_OUT"
    status_code = status.HTTP_408_REQUEST_TIMEOUT
    message = "Request Timed Out"


class OperationFailedException(CustomBaseException):
    code = "OPERATION_FAILED"


class BadRequestException(CustomBaseException):
    code = "BAD_REQUEST"
    status_code = status.HTTP_400_BAD_REQUEST


class InvalidInputException(CustomBaseException):
    code = "UNPROCESSABLE_ENTITY"
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY


class NotFoundException(CustomBaseException):
    code = "NOT_FOUND"
    message = "Not Found"
    status_code = status.HTTP_404_NOT_FOUND


class InvalidDateException(BadRequestException):
    code = "INVALID_DATE"
    message = "Invalid Date"


def exception_handler(exc, context=None):
    """
    Returns the error response when there is an exception

    By default, we handle the REST framework 'APIException' and Django's builtin 'Http404' exception.

    Any unhandled exceptions will be caught and logged by this handler and 'OperationException' is
    raised accordingly the view or process behind the triggered the actual error.
    """

    if isinstance(exc, ValidationError):
        exc = InvalidInputException(errors=exc.detail)

    if not isinstance(exc, (APIException, CustomBaseException)):
        raise exc

    code = getattr(exc, "code", "")
    message = getattr(exc, "message", "")
    error_code = getattr(exc, "error_code", "")
    errors = getattr(exc, "errors", [])

    # If the existing code is not sufficient
    if not code and isinstance(exc, APIException):
        if hasattr(exc, "get_codes"):
            codes = exc.get_codes()
            if isinstance(codes, str):
                code = codes
            else:
                """
                iter() will generate iteration on the dict value. And next() will pick the first key from that list.
                """
                code = next(iter(codes))

        # If no default_code was provided
        code = code or getattr(exc, "default_code", "OPERATION_FAILED")
        code = code.upper()

    if isinstance(exc, MethodNotAllowed):
        code = "NOT_ALLOWED"
    elif isinstance(exc, NotFound):
        code = "NOT_FOUND"

    data = dict(
        message=message,
        errors=errors,
        code=code,
        error_code=error_code,
    )

    return Response(data, status=exc.status_code)
