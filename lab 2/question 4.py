string=input("Enter a String : ")

count = {}

for s in string:
  if s in count:
    count[s] += 1
  else:
    count[s] = 1

for key in count:
  if count[key] > 1:
    print (key, count[key])