from email.utils import localtime
from threading import local
import time

# time()
# number of seconds passed since 1970.1.1 00:00:00
print(time.time())

# gmtime(seconds) localtime(seconds)
# accept number of seconds passed since 1970.1.1
# return struct_time object with the following properties
# tm_year tm_mon tm_mday tm_hour tm_min tm_sec tm_wday tm_yday tm_isdst
print(time.gmtime(time.time()))
print(time.localtime())

# mktime(struct_time object)
# returns the number of seconds passed from 1970.1.1 to the time represented by struct_time object
print(time.mktime(time.localtime()))

# strftime(string with format character %, struct_time)
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# strptime("%a %b %d %H:%M:%S %Y")
# returns struct_time object
print(time.strptime("Tue Sep 09 19:34:21 2003"))