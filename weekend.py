import datetime

#now = datetime.datetime.now()
#
#date = now.date()
#time = now.time()
#today = datetime.datetime.today()
#
#print now
#print date, time, today
#print datetime.datetime.combine(date, time)

now = datetime.datetime.now()
#date = datetime.date(now)
#day = datetime.day(now)
print now
#print day
#print date

day_difference = datetime.timedelta(days=2)
two_days_from_now = now + day_difference
day_of_the_week = datetime.date.today().strftime("%A")

day_of_the_week = "Friday"

if day_of_the_week == "Thursday":
    two_business_day_from_now = now + datetime.timedelta(days=4)
    print two_business_day_from_now

if day_of_the_week == "Friday":
    two_business_day_from_now = now + datetime.timedelta(days=5)
    print two_business_day_from_now


print "Today: " + str(now)
print "Two days from now: " + str(two_days_from_now)
print "Two business days from now: " + str(two_business_day_from_now)


today = datetime.datetime.weekday(now)
print "Day code: ", today
print "Day of week: ", day_of_the_week
