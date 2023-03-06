import datetime

# Current date and time
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%d-%m-%Y %H:%M:%S"))

# Current Year
print("Current Year : ")
print(now.year)

# Month of Year
print("Month of Year")
print(now.month)

# Week number of the year
print('Week number of the year : ')
print(now.isocalendar()[1])

# Week day of the week
print("Week day of the week : ")
print(now.isocalendar()[2])

# Day of Year
print("Day of Year : ")
print(now.strftime('%j'))

# Day of Month
print("Day of Month : ")
print(now.strftime("%d"))

# Day of week
print("Day of week : ")
print(now.strftime('%A'))