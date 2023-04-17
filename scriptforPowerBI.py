import sys  # for utf8
sys.stdout.reconfigure(encoding='utf-8')


#################### power BI ############
from pytrends.request import TrendReq
# add my parameters
trend = TrendReq(hl='fa', tz=330,)

# keyword list
kw_list = ['همراه من', 'ایرانسل من']
# kw_list = ['mci', 'irancell']

# create payload
trend.build_payload(
    kw_list, cat=0, timeframe='2010-01-01 2023-03-03', geo='', gprop='')

# create a dataframe of google trends
data = trend.interest_over_time()
data = data.reset_index()
############### end PowerBI #############

print(data)
