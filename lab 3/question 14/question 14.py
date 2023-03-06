with open('./question 14/file1.txt') as fh1, open('./question 14/file2.txt') as fh2:
    
    for line1, line2 in zip(fh1, fh2):
        # line1 from file1.txt, line2 from file2.txt
        print( line1 + line2 )