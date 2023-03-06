import random

is_correct=True

random_num = random.randint(1, 9)

while(is_correct):
    
    user_guess=int(input("Guess a Number (1-9) :"))
    
    if user_guess > random_num :
        print('You Guessed Too High')
        
    elif user_guess < random_num :
        print('You Guessed Too Low')
        
    else:
        print('You Guessed Exactly Correct')
        is_correct=False    