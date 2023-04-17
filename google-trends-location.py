# import matplotlib
import plotly.express as px
import locale
import sys  # for utf8

from pytrends.request import TrendReq
import pandas as pd
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

for Year in range(2020, 2023+1):
    timeslice = str(Year) + "-01-01 " + str(Year) + "-12-30"

    # create payload
    # trend.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='', gprop='')
    trend.build_payload(
        kw_list, cat=0, timeframe=timeslice, geo='IR', gprop='')
    by_region = trend.interest_by_region(
        resolution='CITY', inc_low_vol=True, inc_geo_code=False)
    # print(trend.suggestions(kw_list))
    # print(by_region.head(200))

    # create a dataframe of google trends
    df1 = by_region[by_region["ایرانسل"] > 0]
    df1 = df1.assign(Years=Year)
    appended_data = [appended_data, df1]
    appended_data = pd.concat(appended_data)
    # appended_data = appended_data.append(df1, ignore_index=True)

appended_data = appended_data.reset_index()
print(appended_data)
