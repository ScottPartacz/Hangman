# %%
import time
import random

# varaibles
wins = 0
loses = 0
menuinput = 0
wordsused = []

#program loop
while True:
    #opening th wordlist file and picking a random word
    f = open("wordlist.txt")
    words = f.readlines()
    word = words[random.randint(0,len(words) - 1)]
    flag3 = False
    #making sure we don't use the same word
    for x in wordsused:
        if word is x:
            flag3 = True
            break

    if flag3:
        continue

    wordsused.append(word)

    #print(word) #testing
    #close file
    f.close()

    # varaibles
    lifes = 7
    partical_word = list(word)
    # removing the "\n" char
    del partical_word[len(partical_word) - 1]
    guess = ""
    display_word = list("_") * (len(word)-1)
    #print(partical_word)
    guesses = 0
    guesslist = [" "]
    # single game loop
    while (True):
        #display image of lives
        if lifes == 7:
            print("-------")
            print("|   |")
            print("|")
            print("|")
            print("|")
            print("|")
            print("-------")
        elif lifes == 6:
            print("-------")
            print("|   |")
            print("|   O")
            print("|")
            print("|")
            print("|")
            print("-------")
        elif lifes == 5:
            print("-------")
            print("|   |")
            print("|   O")
            print("|   |")
            print("|")
            print("|")
            print("-------")
        elif lifes == 4:
            print("-------")
            print("|   |")
            print("|   O")
            print("|   |")
            print("|   |")
            print("|")
            print("-------")
        elif lifes == 3:
            print("-------")
            print("|   |")
            print("|   O")
            print("|  \|")
            print("|   |")
            print("|")
            print("-------")
        elif lifes == 2:
            print("-------")
            print("|   |")
            print("|   O")
            print("|  \|/")
            print("|   |")
            print("|")
            print("-------")
        elif lifes == 1:
            print("-------")
            print("|   |")
            print("|   O")
            print("|  \|/")
            print("|   |")
            print("|  /")
            print("-------")
        counter = 0
        flag = True
        flag2 = False 

        print("lifes remaining: " + str(lifes) + "\n")
        print(display_word)
        print("\n")

        #input guess
        print("please enter your guess\n")
        time.sleep(1)
        guess = input()

        #check to see if you guess this already
        errorinput = 0
        for x in guesslist:
            if guess is x:
                flag2 = True
                errorinput = 1
                break
            if (guess.isalpha()) is False:
                flag2 = True
                errorinput = 2
                break
            if len(guess) > 1:
                flag2 = True
                errorinput = 3 
                break
        else:
            guesslist.append(guess)
        
        if flag2:
            if errorinput == 1:
                print("you guessed that already silly\n")
            elif errorinput == 2:
                print("thats not a letter silly\n")
            elif errorinput == 3:
                print("thats more then one letter silly\n")
            continue
        
        #checks to see if the guess is in the word
        for x in partical_word:
            if guess is x:
                display_word[counter] = guess
                flag = False
            counter += 1

        # if not lose one life
        if(flag):
            lifes = lifes - 1

        #keep track of guess
        guesses += 1

        # checks if you lost
        if lifes == 0:
            print("You ran out of lives sorry\n")
            print("the word was: " + word)
            print("-------")
            print("|   |")
            print("|   O")
            print("|  \|/")
            print("|   |")
            print("|  / \ ")
            print("-------")
            loses += 1
            break
        #checks if you won
        if display_word == partical_word:
            print("you won\n")
            print("the word was: " + word)
            print("you guessed: " + str(guesses) + " times\n")
            wins += 1
            break
    # W/L
    print("W/L:\n")
    print("wins: " + str(wins))
    print("loses: " + str(loses) + "\n")

    #menu
    print("1: done")
    print("press anything else: play again\n")
    time.sleep(1)
    menuinput = input()
    if menuinput == "1":
        print("thanks for playing")
        break    


