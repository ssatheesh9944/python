with open('./question 8/test.txt', 'r') as infile:
        words = infile.read().split()
        longest_word = (max(words, key=len))
        print(longest_word)