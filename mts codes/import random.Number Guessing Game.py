import random


while 1 == 1:
    print('welcome to the Number Guess game')
    true_guess = random.randint(1,10)
    guess_count = 1
    guess_limit = 4
    rerun = "y"
    guess = int(input("enter a guess between 1 and 10:"))
    start = 'y'

    while guess_count != guess_limit:
    
        if guess == true_guess:
            print("your guess is correct")
            print("you guessed right on count ", guess_count)
            print("YOU WIN")
        
            restart = str(input("Do you wish to start again?(y/n):"))
            if restart == rerun:
                print("restarting...")
            
            else:
                break
        
        while guess != true_guess:
            if guess == 100:
                print(true_guess, "cheat")
                guess = int(input("enter another guess:"))
            
            elif guess > true_guess:
                print("your guess is higher")
                guess = int(input("enter another guess:"))
            
            elif guess < true_guess:
                print("your guess is lower")
                guess = int(input("enter another guess:"))

        
            else:
                print("invalid input")
                guess = int(input("enter another guess:"))
        
            break
        guess_count += 1
    continue 

while guess != true_guess:  
    if guess_count == 1 + guess_limit:
        print("YOU LOSE")
        restart = str(input("try again?(y/n):"))
        if restart == rerun:
            print("restarting...")
            break
            
        else:
            break
    continue

print("GAME OVER")
  
    
     
   
      
             