# import matplotlib
import pandas as pd
from pytrends.request import TrendReq
import plotly.express as px
import locale
import sys  # for utf8
import datetime
from dateutil.relativedelta import relativedelta

appended_data = pd.DataFrame()
# set utf8 for terminal
sys.stdout.reconfigure(encoding='utf-8')
print("به عنوان کدینگ پیش فرض فعال شد", sys.getdefaultencoding())
# display all rows from dataframe using Pandas
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
# add my parameters
trend = TrendReq(hl='fa', tz=330,)
# keyword list
kw_list = ['همراه اول', 'ایرانسل']

########### while ##############
start_date = datetime.date(2020, 1, 1)
end_date = datetime.date(2023, 3, 1)
delta = datetime.timedelta(days=1)

while start_date <= end_date:

    timeslice = str(start_date) + " " + \
        str(start_date + relativedelta(months=1))
    print(timeslice)
    trend.build_payload(
        kw_list, cat=0, timeframe=timeslice, geo='', gprop='')
    # create a dataframe of google trends suggestions
    # df = pd.DataFrame(trend.suggestions('همراه اول'))
    # df.head()
    # print(df)
    # print("*" * 55)
    rq = trend.related_queries()
    rq.values()
    df = pd.DataFrame(rq.get('ایرانسل').get('rising'))
    df.head(100)
    # print(df)

    df = df.assign(date=start_date)
    df['operator'] = 'ایرانسل'

    # df=df.assign(**{'datee': start_date, 'col2_new_2': 'dogs', 'col3_new_3': 3})
    # df.insert(2,"test", start_date, False)
    # df.insert(3,"test2", start_date, False)

    appended_data = [appended_data, df]
    appended_data = pd.concat(appended_data)

    # appended_data = appended_data.append(df1, ignore_index=True)
    start_date = start_date + relativedelta(months=+1)
appended_data = appended_data.reset_index()
print(appended_data)

appended_data.to_csv('monthlyqueryirancell.csv')
