from datetime import datetime


def get_current_date_as_integer():
    current_date = datetime.now().timestamp()
    return int(current_date)


from rest_framework.views import exception_handler


def biz_exception_handler(exc, context):
    # Call the default exception handler first to get the standard error response
    response = exception_handler(exc, context)

    if response is not None:
        # Customize the structure of the error response
        customized_response = {
            'detail': response.data.get('detail', 'An error occurred.'),
        }
        response.data = customized_response

    return response
