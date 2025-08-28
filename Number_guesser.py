import random
import time
import sys
loop_lock = True
rand_num = random.randint(1, 100)
guess_count = 0
print("Welcome to the number guessing game! Would you like to play?")
print("This is a game by jpsAR")
time.sleep(0.5)
print("I am thinking of a number between 1 and 100.")
while loop_lock == True:
    input_var = input("What do you think it is?:")
    if int(input_var) == rand_num:
        guess_count = guess_count + 1
        print("Awsome! The number was " + str(rand_num) + "! Good job there! You got this in: " + str(guess_count) + " guesses.")
        time.sleep(1)
        loop_lock = False
    elif int(input_var) > 100:
        print("That's out of range! you can't guess higher then 100.")
    elif int(input_var) < 1:
        print("That's out of range! you can't guess lower then 1.")    
    elif int(input_var) < rand_num:
        print("Hey! That's smaller then my number, try again!")
        guess_count = guess_count + 1
        if guess_count > 9999:
            print("ouch! you ran out of guesses! try again next time.")
            break
    elif int(input_var) > rand_num:
        guess_count = guess_count + 1
        print("Hey! That's bigger then my number, try again!")
        if guess_count > 9999:
            print("ouch! you ran out of guesses! try again next time.")   
sys.exit("Thanks for playing! I hope you had a fun time!")
