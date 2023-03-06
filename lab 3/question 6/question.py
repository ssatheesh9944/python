f = open("./question 6/test.txt","r")
str=""

for i in range(0,100):
    str=str + f.read(i)

print(str)