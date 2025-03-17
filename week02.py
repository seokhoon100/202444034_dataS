# alt + shift + F10
import random

answer = random.randint(1, 1000)
win = False

for guesses in range(10):
    print(f"{10 - guesses}LIFE LEFT | NUMBER : ", end = '')
    guess = int(input())

    if answer == guess:
         print("WIN")
         win = True
         break

    elif answer > guess:
        print("LOW")

    elif answer < guess:
        print("HIGH")