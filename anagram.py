'''
Code Name : anagram.py
Purpose   : Game that creates a anagram game. The user is given a jumbled word which needs to be corrected.
Initial Version : 10-November-2017
Created By      : Avantika Joshi
'''

#The script below creates the game of Anagram
import random
try:
    user_name = input("Please enter your name\n")
    print ("Hi " + user_name)
    print ("WELCOME")
    choice = input("Would you like to know the rules of the games? \n\n 1. Yes, I would love to. \n\n 2. No, I already know\n")
    if choice == "1":
        print (" You will be given a word in jumbled up form and your job is to find the word")
        print ("\n For each word, you have 3 attempts, after which the correct word will be shown")
        print ("\n Press Ctrl + C or Ctrl + D to end the game")
    else:
        # Open the file containing all the words
        with open("words.txt","r") as f:
            words = [line.strip() for line in f]
        ind = -1
    while (1):
        # Find the length of the list containing words
        length = len(words)
        index = random.randint(0,length-1)
        word = words[index]
        random_word = "".join(random.sample(words[index],len(words[index])))
        if random_word == words[index]:
            continue
        attempts = 4
        while (attempts > 0):
            prev_ind = ind
            hint_str = ""
            user_entry = input("\n\n What is the word : " +random_word +"\n")
            if user_entry == word :
                print ("Congratulations ! The word is right\n")
                attempts = 0
                continue
            else:
                if attempts == 1:
                    print ("No more attempts left")
                    print ("\nThe word was " + words[index])
                    attempts = 0
                    continue
                else:
                    print ("You have " + str(attempts - 1) + " more attempts left. Please try again :)")
                    word_length = len(word)
                    if attempts < 4 :
                        while (ind == prev_ind):
                            ind = random.randint(0,word_length-1)
                    else:
                        ind = random.randint(0,word_length-1)
                    correct_word_hint = word[ind]
                    for i in range(0,word_length):
                        if i==ind:
                            hint_str = hint_str + correct_word_hint
                        else:
                            hint_str = hint_str + "*"
                    print ("Hint : " + hint_str)
            attempts = attempts - 1
except EOFError:
    print ("The Game Ends")
    print ("Thank you for playing ")
except KeyboardInterrupt:
    print ("The Game Ends")
    print ("Thank you for playing ")
