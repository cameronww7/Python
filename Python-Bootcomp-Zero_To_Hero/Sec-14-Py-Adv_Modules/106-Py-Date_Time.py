from __future__ import print_function
import datetime

"""
 Prompt 106-Py-Date_Time
"""

print("106-Py-Date_Time")

"""
datetime module

Python has the datetime module to help deal with timestamps in 
your code. Time values are represented with the time class. 
Times have attributes for hour, minute, second, and microsecond. 
They can also include time zone information. The arguments to 
initialize a time instance are optional, but the default of 0 
is unlikely to be what you want.

time

Let's take a look at how we can extract time information from 
the datetime module. We can create a timestamp by specifying 
datetime.time(hour,minute,second,microsecond)
"""
print("\ndatetime.time(4, 20, 1)")
print("- - - - - - - - - - ")
t = datetime.time(4, 20, 1)

# Let's show the different components
print(t)
print('hour  :', t.hour)
print('minute:', t.minute)
print('second:', t.second)
print('microsecond:', t.microsecond)
print('tzinfo:', t.tzinfo)


print('Earliest  :', datetime.time.min)
print('Latest    :', datetime.time.max)
print('Resolution:', datetime.time.resolution)


"""
Dates

datetime (as you might suspect) also allows us to work with date 
timestamps. Calendar date values are represented with the date 
class. Instances have attributes for year, month, and day. It is 
easy to create a date representing today’s date using the today() 
class method.
"""
print("\ndatetime.date.today()")
print("- - - - - - - - - - ")
today = datetime.date.today()
print(today)
print('ctime:', today.ctime())
print('tuple:', today.timetuple())
print('ordinal:', today.toordinal())
print('Year :', today.year)
print('Month:', today.month)
print('Day  :', today.day)


print('Earliest  :', datetime.date.min)
print('Latest    :', datetime.date.max)
print('Resolution:', datetime.date.resolution)


print("\ndatetime.date(2015, 3, 11)")
print("- - - - - - - - - - ")
d1 = datetime.date(2015, 3, 11)
print('d1:', d1)

d2 = d1.replace(year=1990)
print('d2:', d2)
