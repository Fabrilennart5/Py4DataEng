# Dattime is and important topic in data engineering
# We will see how to work with datetime in python

from datetime import datetime
from datetime import timedelta

# this is how we generate a datetime now and print it

current_datetime = datetime.now()
print(current_datetime)


def substractHours(date, hours):
    # this is how we substract hours
    return date - timedelta(hours=hours)


# if we print this function
print(substractHours(current_datetime, 2))

# we can also format the way this is displayed


def formatdate(date):
    return date.strftime("%Y/%m/%d %H:%M:%S")


# if we print this, we are going to get a formatted date
print(formatdate(substractHours(current_datetime, 2)))
