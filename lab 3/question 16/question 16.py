def remove_newlines(fname):
    
    flist = open(fname).readlines()
    return [s.rstrip('\n') for s in flist]

print(remove_newlines("./question 16/test.txt"))
