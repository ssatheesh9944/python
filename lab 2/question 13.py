from itertools import combinations

list_items=["M", "A", "S",]
subs = []
for i in range(0, len(list_items)+1):
	temp = [list(x) for x in combinations(list_items, i)]
	if len(temp)>0:
	    subs.extend(temp)
print(subs) 