from colorama import Fore, Back, Style
import random

lyrics = [{"you": "All I want for Christmas is ___"},
          {"give": "Never going to ____ you up"},
          {"lose my mind": "Y'all going to make me ____ __ ____ up in here, up in here"},
          {"2G": "Cash Money taking over for the '99 and the __"},
          {"more money": "The ____ _____ we come across the more problems we see"},
          {"99 problems": "I got __ ________ but a bitch aint one"},
          {"Bible": "Beat your ass and hide the _____ if GOD's watching"},
          {"rock": "We will, we will ____ you"},
          {"entertain": "With the lights out its less dangerous. Here we are now _________ us"},
          {"love": "And I will always ____ you"},
          {"Sunny days": "____ _____, everybody loves them. Can you stand the rain?"}
          ]

count = 0

def get_lyrics(count, list):
    random_choice = random.choice(list)
    key, value = random_choice.popitem()
    attempt(count, key, list, value)
    return  key, list, value

def attempt(count, key, list, value):
    while True:
        ans = input(Fore. GREEN + f"\n{value}\n").lower()
        if ans == key.lower():
            count += 1
            print(Fore.CYAN + f"Well done, it only took you {count} attempts!" + Style.RESET_ALL)
            break
        else:
            count += 1
    exit = input("Enter 1 to play again, or 2 to exit:\n")
    if exit == "1":
        count = 0
        get_lyrics(count, list)
    elif exit == "2":
        print("\nThanks for playing" + Fore.YELLOW + " Fill-In The Blank Lyrics" + Style.RESET_ALL + ". Goodbye!\n")
    else:
        print("Invalid input.")

print(Fore.YELLOW + "       ***   Fill-In The Blank Lyrics!   ***\n (Guess the blank lyrics, see if you know your stuff)" + Style.RESET_ALL)
get_lyrics(count, lyrics)