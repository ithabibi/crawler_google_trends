import datetime
from dateutil.relativedelta import relativedelta


start_date = datetime.date(2020, 1, 1)
end_date = datetime.date(2022, 1, 4)
#delta = datetime.timedelta(days=1)

while start_date <= end_date:
    print(start_date)
    start_date = start_date + relativedelta(months=+1)
