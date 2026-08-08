from datetime import datetime


def calculate_account_age(created_at: str):

    """
    Returns account age in years.
    """

    created = datetime.strptime(
        created_at,
        "%Y-%m-%dT%H:%M:%SZ"
    )

    today = datetime.utcnow()

    return (today - created).days // 365


def safe_divide(a, b):

    """
    Prevent division by zero.
    """

    if b == 0:
        return 0

    return round(a / b, 2)


def format_date(date_string: str):

    """
    Convert GitHub date into readable format.
    """

    dt = datetime.strptime(
        date_string,
        "%Y-%m-%dT%H:%M:%SZ"
    )

    return dt.strftime("%d-%m-%Y")
