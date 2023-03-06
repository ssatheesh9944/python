from datetime import datetime

ts = int("1584101485")
print(datetime.utcfromtimestamp(ts).strftime('%d-%m-%Y'))
