# import matplotlib
from pytrends.request import TrendReq
import plotly.express as px
import locale
import sys  # for utf8
import pandas as pd


# set utf8 for terminal
sys.stdout.reconfigure(encoding='utf-8')
print("به عنوان کدینگ پیش فرض فعال شد", sys.getdefaultencoding())
print("برای چاپ در خروجی پشتیبانی شد", sys.stdout.encoding)

# # set Font for matplotlib
# matplotlib.rc('font', family='Arial')

# display all rows from dataframe using Pandas
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# add my parameters
trend = TrendReq(hl='fa', tz=330,)

# keyword list
kw_list = ['همراه اول', 'ایرانسل']
# kw_list = ['mci', 'irancell']

# create payload
# trend.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='', gprop='')
trend.build_payload(
    kw_list, cat=0, timeframe='today 1-m', geo='', gprop='')

print("kw_list, cat=0, timeframe='2006-01-01 2023-03-03', geo='IR', gprop=''")

# create a dataframe of google trends
df = pd.DataFrame(trend.suggestions('همراه اول'))
df.head()
print(df)

print("*" * 55)

rq = trend.related_queries()
rq.values()
df = pd.DataFrame(rq.get('همراه اول').get('rising'))
df.head(100)
print(df)
