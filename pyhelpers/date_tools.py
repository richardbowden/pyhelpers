from datetime import datetime

def get_length_of_time(start_date, end_date=None, days_in_year=365, days_in_month=30):
    """
    start_date and end_date should be a datetime object with the day of month
    always being 1, as all we need is to calc years and months between two dates
    """
    if end_date == None:
        d = date.today()
        end_date = datetime(d.year, d.month, 1)

    if start_date == end_date:
        return 0,0

    if start_date > end_date:
        raise Exception('Start date cannot be greater than end date')

    total_days = (end_date - start_date).days

    years, r = divmod(total_days, days_in_year)
    months = round(r / days_in_month)

    return years, months
