class ErrorEnum:
    class HTTP:
        METHOD_NOT_ALLOWED = "METHOD_NOT_ALLOWED"
        THROTTLED = "HTTP_THROTTLED"
        UNAUTHORIZED = "UNAUTHORIZED"
        UNAUTHORIZED = "UNAUTHORIZED"
        TOO_MANY_REQUESTS = "TOO_MANY_REQUESTS"
        PERMISSION_DENIED = "PERMISSION_DENIED"
        FORBIDDEN = "FORBIDDEN"

    class LoginAPIView:
        INVALID_CREDENTIALS = "LOGIN_INVALID_CREDENTIALS"

    class RefreshAPIView:
        EMPTY_REFRESH = "REFRESH_EMPTY_REFRESH"
        INVALID_REFRESH_TOKEN = "REFRESH_INVALID_REFRESH_TOKEN"

    class GetItemListAPIView:
        INVALID_LIMIT_OR_OFFSET = "GET_ITEM_LIST_INVALID_LIMIT_OR_OFFSET"
