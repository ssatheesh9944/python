#create a tuple
tuplex = tuple("mashup stack")
print(tuplex)

#get index of the first item whose value is passed as parameter
index = tuplex.index("s")
print(index)

#define the index from which you want to search
index = tuplex.index("s", 5)
print(index)

#define the segment of the tuple to be searched
index = tuplex.index("a", 7, 11)
print(index)

#if item not exists in the tuple return ValueError Exception
index = tuplex.index("y")