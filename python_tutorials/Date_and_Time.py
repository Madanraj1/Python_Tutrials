#for time
import time
#for calendar 
import calendar
#12:00am january 1, 1970
seconds = time.time()
#To print seconds since 1970
print("seconds since 12:00am january 1, 1970 ",seconds)

#to print your local time
localtime = time.localtime()
print("local time",localtime)

#To print your local time in format
localtime = time.asctime(time.localtime(time.time()))
print(localtime)

#to print calendar of any year and month
cal = calendar.month(2019,2)
print("calendar","\n",cal)