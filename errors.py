
"""
There is 3 categories of errors :

+ System-level Errors - 500:
        - Database Connection Issue.
        - Backend Service Connection Issue.
        - Fatal Error

+ Business Logic Errors 429:
        - Rate-limited
        - Request Fulfilled but no results were found.
        - Business Related reason to deny access to information.

+ API Request Formatting Errors 400:
        - Required request parameters are missing.
        - Combined request parameters are invalid together.

+ Authorization Errors 401:
        - OAuth credentials are invalid for request.
        - Token has expired.

"""


ERRORS = {
    ""
}
