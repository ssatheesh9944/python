string = input("Enter a String : ")

dict = {}

for i in string:
    
    if i in dict:
        dict[i] += 1

    else:
        dict[i] = 1

print(dict)