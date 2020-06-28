import random
Words = ["apple", "windows", "microsoft", "samsung", "tesla", "spacex", "nvidia", "intel", "siemens", "nokia",
         "oracle", "google", "lenovo", "monster", "amazon", "spotify""computer", "mouse", "keyboard", "screen"]
         # Enter the words to be found in the hangman.

randomly_selected_words = random.choice(Words) # We chose a random word using the random function.
letters_guessed = ["a", "b", "c", "d", "e", "f"]
alphabet = ("abcdefghijklmnopqrstuvwxyz")      # Enter the letters in your Alphabet.
additive_lives = 5  # The length of the randomly selected word and the sum of the number typed here determine the number of attempts by the user.

#   When all of the letters in the randomly selected word are found, 
# Return True to indicate to the user that the word has been found.
def Is_Word_Guessed(randomly_selected_words, letters_guessed):
    list = []
    counter = 0
    for i in randomly_selected_words:
        list.append(i)
        if list[counter] not in letters_guessed:
            return False
        counter += 1
    return True

#  The letter length of the randomly selected word was taken and the number of "_" printed.
#  In addition, if the letter chosen by the user exists in the randomly selected word, the 
# value "_" is replaced with the letter chosen by the user.
def Get_Guessed_Word(randomly_selected_words, letters_guessed):
    list = []
    counter = 0
    for i in randomly_selected_words:
        list.append(i)
        if list[counter] not in letters_guessed:
            list.pop(counter)
            list.append("_ ")
        counter += 1
    list = "".join(list)
    return list

# The letters used in this function have been removed from the alphabet list.
def Get_Available_Letters(letters_guessed):
    list = []
    counter = 0
    for i in alphabet:
        list.append(i)      
        if list[counter] in letters_guessed:    #   The letter used was removed from the list by specifying the location 
            list[counter] = ("")                # of the letter used in the list and replacing that value with a space.  
        counter += 1                
    list = "".join(list)            
    return list

def Game_Control():
    lives = additive_lives + len(randomly_selected_words)
    print("Welcome to the game Hangman!")
    print(f"I am thinking a word that is {len(randomly_selected_words)} letters long")
    print(f"You have {lives} guesses left")
    print("Available letters: abcdfghjlmnoqtuvwxyz")
    letters_used = []
    letters_guessed = []
    control = False
    while lives > 0:
        lives -= 1
        letter = input("Please guess a letter: ")
        letters_guessed.append(letter)
        Get_Guessed_Word(randomly_selected_words, letters_guessed)
        print(f"\nYou have {lives} guesses left")
        print("Available letters: "+ Get_Available_Letters(letters_guessed))

        if letter in randomly_selected_words and letter not in letters_used:
            print("Good guess: " + Get_Guessed_Word(randomly_selected_words, letters_guessed))
            letters_used.append(letter)

        elif letter in letters_used:
            print("Oops! You've already guessed that letter.")
    
        else:
            print("Wrong, try again. " + Get_Guessed_Word(randomly_selected_words, letters_guessed))
            letters_used.append(letter)

        # The control variable was assigned to resolve the error that would occur if the game was won with the last right.
        if Is_Word_Guessed(randomly_selected_words, letters_guessed) == True:
            print("Congratulations, you won! ")
            control = True  
            break

    if lives == 0 and control == False:
        print("You Lose")
        print(f"Word: {randomly_selected_words}")

Game_Control()
