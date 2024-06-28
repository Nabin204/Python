from datetime import datetime
now = datetime.now()
print("Current datetime : ",now)

date = now.date()
time = now.time()
print("Today's date is :",date)
print("Current time is :",time)

year = date.year
month = date.month
day = date.day
hour = time.hour
minute = time.minute
second = time.second

print("Year :",year)
print("Month :",month)
print("Day :",day)
print("Hour :",hour)
print("Minute :",minute)
print("Second :",second)

from datetime import date
today = date.today()
print("Today's date :",today)

import time
t = time.time()
print("Current time :",time.ctime(t))