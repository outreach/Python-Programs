import datetime

# now = datetime.datetime.now()
now = datetime.datetime.now() + datetime.timedelta(days=7)
two_days_from_now = now + datetime.timedelta(days=2)
day_of_the_week = now.strftime("%A")

# Calculate business days
if day_of_the_week == "Monday" or day_of_the_week == "Tuesday" or day_of_the_week == "Wednesday":
    two_business_day_from_now = now + datetime.timedelta(days=2)

if day_of_the_week == "Thursday":
    two_business_day_from_now = now + datetime.timedelta(days=4)

if day_of_the_week == "Friday":
    two_business_day_from_now = now + datetime.timedelta(days=5)

if day_of_the_week == "Saturday":
    two_business_day_from_now = now + datetime.timedelta(days=4)

if day_of_the_week == "Sunday":
    two_business_day_from_now = now + datetime.timedelta(days=3)


#print "Today: " + str(now)
print "Today: " + now.strftime("%A, %B %e, %Y %r")
#print "Two days from now: " + str(two_days_from_now)
print "Two days from now: " + two_days_from_now.strftime("%A, %B %e, %Y %r")
print "Two business days from now: " + two_business_day_from_now.strftime("%A, %B %e, %Y %r")
print "Day code: " + now.strftime("%w")