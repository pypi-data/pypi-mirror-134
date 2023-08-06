from datetime import datetime, timedelta, date


def format_date(date: str) -> datetime:
    """
    Format string to datetime object
    :raises ValueError if date is not of valid format
    """
    if date == 'today':
        return datetime.today()
    if date == 'yesterday':
        return (datetime.today() - timedelta(days=1))
    if 'daysAgo' in date:
        try:
            nb_days = int(date.replace('daysAgo', '').strip())
            return (datetime.today() - timedelta(nb_days))
        except (ValueError, TypeError) as err:
            raise ValueError(f'Number of days must be int', {err}) from err
    elif '-' in date:
        try:
            return datetime.strptime(date, '%Y-%m-%d')
        except (ValueError, TypeError) as err:
            raise ValueError(f'Datetime is not of format "%Y-%m-%d", {err}') from err
    else:
        raise ValueError(f'Datetime is not of format "%Y-%m-%d", "today", "yesterday" or "X daysAgo". value "{date}" is not supported yet.')


def daterange(start_date: date, end_date: date):
    """
    Create an iterator over date between start date and end data. Both dates are included.

    """

    for n in range(int((end_date - start_date).days) + 1):
        yield start_date + timedelta(n)
