# Append-adds at last
file1 = open("./question 3/test.txt", "a")  # append mode
file1.write("\nBanana")
file1.close()
 
file1 = open("./question 3/test.txt", "r")
print("Output of Readlines after appending")
print(file1.read())
print()
file1.close()
