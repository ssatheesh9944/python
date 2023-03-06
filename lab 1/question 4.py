n=int(input("Enter an integer:"))
print("The divisors of the number are:")
num_list = []
for i in range(1,n+1):
    if (n%i==0):
        num_list.append(i)
print(num_list)        