import datetime

name=input('Enter Your Name :')
age=int(input('Enter Your Age :'))
today = datetime.date.today()
currentyear = today.year
year=currentyear+(100-age)
print(f"Hai {name}. in {year} you turned 100 years old. ")