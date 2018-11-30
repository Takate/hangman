import random

rerun = "Yes"
while rerun == "Yes" or "Y" or "yes" or "YES":

    listOfWords = ["test"]
    guessWord = random.choice(listOfWords)
    guessWordList = list(guessWord)
    #print(guessWordList)

    letterIs = []
    board = [" * " for char in guessWord]

    difficulty = input("\n easy - 15 tries \n medium - 10 tries \n hard - 5 tries \n Please select difficulty: ")

    if difficulty == "easy":
        i = 15
        print(" You choose easy difficulty!")
    if difficulty == "medium":
        i = 10
        print(" You choose medium difficulty!")
    if difficulty == "hard":
        i = 5
        print(" You choose hard difficulty!")

    print("-" * 60)
    print(" The word has {0} letters\n".format(len(guessWord)))
    print("      "+" * " * len(guessWord))
    print("-" * 60)
        
    while i > 0:
        print("\n You still have {0} lives!".format(i))
        letter = input(" Please, insert a letter: ")
        if len(letter) == 1:
            if letter in guessWord and letter in letterIs:
                print(" Sorry, you have already guessed the letter!")
                print("-" * 60)
                print("      " + board)
                print("-" * 60)
                print(" Already used words")
                print("".join(letterIs))
            if letter in guessWord and letter not in letterIs:
                print(" You guessed the letter correctly!\n")
                board = [char if char == letter or char in letterIs else " * " for char in guessWord]
                #print(board)
                if board == guessWordList:
                    print("_" * 60)
                    print("\n Congratulations! You guessed the word {0}!".format(guessWord))
                    print("_" * 60)
                    rerun = input("Wanna play again? (Yes/No): ")
                    if rerun == "Yes" or "Y" or "yes" or "YES":
                        print("\n Nice! Restarting the game! :) Good luck ;)")
                        break
                    if rerun == "No" or "N" or "no" or "NO":
                        print("\n Thanks for playing! :)")
                        break
                board = "".join(board)
                print("-" * 60)
                print("      " + board) # display board
                print("-" * 60)
                print(" Already used words")
                letterIs.append(letter) # for checking already said letters
                print("".join(letterIs))
                
            if letter not in guessWord:
                print(" Bad luck!")
                i -= 1
                board = "".join(board)
                print("-" * 60)
                print("      " + board)
                print("-" * 60)
                print(" Already used words")
                print("".join(letterIs))
        else:
            print(" Please write only one letter!")

