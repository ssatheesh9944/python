def LastNlines(fname, N):
    
    with open(fname) as file:
        for line in (file.readlines() [-N:]):
            print(line, end ='')
            
            
            
LastNlines("./question 4/test.txt", 1)            