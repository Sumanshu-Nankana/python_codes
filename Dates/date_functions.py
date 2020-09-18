from datetime import datetime, timedelta

current_time = datetime.now()

print('Current Time is: ' + str(current_time))

# we can use timedelta to add or remove days or weeks to a date
one_day = timedelta(days=1)
yesterday = current_time - one_day
print('Yesterday is: ' + str(yesterday))

one_week = timedelta(weeks=1)
last_week = current_time - one_week
print('Last week is: ' + str(last_week))