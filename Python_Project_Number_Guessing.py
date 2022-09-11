#Python Looping Project -Number Guessing
#The project is a game that will generate a random number in specified range and user must guess the number after receiving the hints.Everytime user guess  wrong more hint will be provided but reducing the score

import random

attempt_list=[]
def show_score():
    if len(attempt_list)<=0:
        print("There is currently no high score, it's yours for the taking!")
    else:
        print("The current high score is {} attempts ".format(min(attempt_list)))

def start_game():
    #generate a random number
    random_number=int(random.randint(1,10))
    print("Hello player")
    player_name=input("what is your name")
    wanna_play=input("Hi {} would you like to  play (yes/No)".format(player_name))
    attempts=0
    show_score()
    while wanna_play.lower()=="yes":
        guess=input("Pick a number between 1 and 10 : ")
        if int(guess) < 1 or int(guess) > 10:
            print("Please guess the number within the range")
        if int(guess) == random_number:
            print("WOW you got it")
            attempts+=1
            attempt_list.append(attempts)
            print("You took {} much attemps till now".format(attempts))
            play_again=input("would like to play(yes/no)")
            attempts=0
            show_score()
            random_number=int(random.randint(1,10))
            if play_again.lower()=="no":
                print("That's cool have a good one")
                break
        elif int(guess) < random_number:
            print("It's lower")
            attempts += 1
        elif int(guess) > random_number:
            print("It's higher")
            attempts+=1
        else:
            print("That's cool, have a good one!")

if __name__=='__main__':
    start_game()
