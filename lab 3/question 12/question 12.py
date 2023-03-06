color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
with open('./question 12/test.txt', "w") as myfile:
        for c in color:
                myfile.write("%s\n" % c)

content = open('./question 12/test.txt')
print(content.read())
