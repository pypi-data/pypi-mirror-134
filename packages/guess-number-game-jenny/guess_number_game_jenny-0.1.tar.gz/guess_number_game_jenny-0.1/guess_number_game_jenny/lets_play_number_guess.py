import random

ans = random.randrange(1,100)
guess = int(input("Findout my number, I'm a number between 1 to 100!"))

while ans is not guess:
    if guess > ans:
        print("I'm a smaller number, try again")
        guess = int(input("Answer: "))
    elif guess < ans:
        print("I'm a larger number, try again")
        guess = int(input("Answer: "))
    else:
        print("You got it right!! It's ",ans)
        
print("You got it right!! It's ",ans)
    
