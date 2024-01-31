from functools import wraps
from fastapi.responses import JSONResponse
from fastapi import status


class CustomException(Exception):
    def __init__(self, message, status_code):
        super().__init__(message)
        self.status_code = status_code


def error_handler(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)

            if result is None:
                return JSONResponse(
                    content={"error": "Resource not found"},
                    status_code=status.HTTP_404_NOT_FOUND)

            return result

        except CustomException(400) as specific_exception:
            return JSONResponse(
                content={"error": str(specific_exception)},
                status_code=status.HTTP_400_BAD_REQUEST)

        except CustomException(422) as another_specific_exception:
            return JSONResponse(
                content={"error": str(another_specific_exception)},
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)

        except Exception as e:
            error_message = f"Internal Server Error: {str(e)}"
            return JSONResponse(
                content={"error": error_message},
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return wrapper
