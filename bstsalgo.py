from datetime import datetime
from dateutil.relativedelta import relativedelta

# first establish how many days in the pre-period (learning) and the post-period (predicting)
dates['pre_period'] = dates['Date published'] - pd.DateOffset(days=20)
dates['post_period'] = dates['Date published'] + pd.DateOffset(days=3)
# adding this extra column for the formatting of the algorithm
dates['datepublished1'] = dates['Date published'] + pd.DateOffset(days=1)

# change all dates to business dates (financial market is closed on weekends and holidays) 
from pandas.tseries.offsets import BDay
dates.pre_period = dates.pre_period.map(lambda x : x + 0*BDay())
dates.post_period = dates.post_period.map(lambda x : x + 0*BDay())
dates.datepublished1 = dates.datepublished1.map(lambda x : x + 0*BDay())
dates = dates.sort_values(by=['Date published'])

# creating lists with all these dates
a = dates['Date published'].tolist()
b = dates['pre_period'].tolist()
c = dates['post_period'].tolist()
d = dates['datepublished1'].tolist()


