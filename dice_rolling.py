import random
score=0
round=0

n=int(input("Enter number of times you want to roll the dice:"))   #rounds
while (round<n):
    
    r = input("Do you want to roll the dice? (YES/NO): ")

    if r.upper() == "YES":
        a = random.randint(1, 6)
        b = random.randint(1, 6)
        print("You rolled the dice and the resultant numbers are:", a, b)
        total_sum=a+b
        score+=total_sum
        round+=1
        
        print(total_sum)
        print(score)
        
    elif r.upper() == "NO":
        print("Ok as you wish!")
    else:
        print("Invalid input! Game Over.")
        break  