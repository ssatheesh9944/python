import datetime

date = datetime.date(2015, 6, 16)
week_number = date.isocalendar().week
print(week_number)