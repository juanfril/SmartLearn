from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        response.data['status_code'] = response.status_code

        if response.status_code == status.HTTP_400_BAD_REQUEST:
            response.data['detail'] = 'Bad request.'
        elif response.status_code == status.HTTP_404_NOT_FOUND:
            response.data['detail'] = 'Not found.'
        # Add more custom error handling as needed

    return response
