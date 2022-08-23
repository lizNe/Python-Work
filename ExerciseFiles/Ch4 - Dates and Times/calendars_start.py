#
# Example file for working with Calendars
# LinkedIn Learning Python course by Joe Marini
#


# TODO: import the calendar module
import calendar

# TODO: create a plain text calendar
c = calendar.TextCalendar(calendar.TUESDAY) # Month starts with this day
# str = c.formatmonth(2022, 1, 0, 0) # format into a string
# print(str)

# # TODO: create an HTML formatted calendar
# hc = calendar.HTMLCalendar(calendar.SUNDAY)
# str = hc.formatmonth(2022, 1)
# print(str)

# TODO: loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month

# for i in c.itermonthdays(2022,8): # goes through all the days in the month. 0000 represents the days that are in that calendar but for the other month
#     print(i)

 
# TODO: The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms

for name in calendar.month_name:
    print(name)

for day in calendar.day_name:
    print(day)

# TODO: Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:

# print("Team meetings will be on:")
# for m in range(1,13): #13 is not inclusive so its 1 - 12
#     cal = calendar.monthcalendar(2022, m) #m is month number # list of weeks that represent the days of the month
#     weekone = cal[0] # first friday has to be in week 1 or week 2
#     weektwo = cal[1]
#     if weekone[calendar.FRIDAY] != 0: # 0 means part of a different month like we seen in the other example listng the dates
#         meetday = weekone[calendar.FRIDAY]
#     else:
#         meetday = weektwo[calendar.FRIDAY]
    
#     print(calendar.month_name[m], meetday)


# text formatted monthly calendat for every month in the current year, using sunday as the first day of the week
import calendar
import datetime

year = datetime.datetime.now().year
cal = calendar.TextCalendar(calendar.SUNDAY)
for m in range(1,13):
    print(cal.formatmonth(year, m, 0, 0,))