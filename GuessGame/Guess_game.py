import random
import Guess_words
import colorama
from colorama import Fore
colorama.init(autoreset=True)
lives = 5
print(f"{Fore.RED}WELCOME {Fore.GREEN}TO {Fore.BLUE}GUESS {Fore.CYAN}GAME")
name = input("Please enter your name : ")
def games(lives):
    val = Guess_words.val
    ans = random.choice(val)
    ans = ans.upper()
    anslen = len(ans)
    dash = "_" * anslen
    print(f"{Fore.MAGENTA}Guess the animal {dash}. It is of {anslen} characters")
    game = True
    a = []
    val1 = dash

    while game:
        inputvalue = input(f"{Fore.BLUE}Enter the character : ")
        inputvalue = inputvalue.upper()
        dis = ""
        for i in ans:
            if i in inputvalue:
                dis += i
                a.append(i)
            elif i in a:
                dis +=i
            else:
                dis += "_"
        print(dis)
        if val1.count("_") == dis.count("_"):
            if inputvalue in dis:
                print(f"{name} you have already used it")
            else:        # lives +=1
                lives -= 1
                print(f"{Fore.RED}{name} you have {lives} lives remaining")
        else:
            val1 = dis
            if "_" in dis:
                print(f"{Fore.GREEN}Good one {name} keep going")

        if "_" not in dis or lives <= 0:
            game = False
            if lives <= 0:
                print(f"Sorry you failed, word is {ans}")
            else:
                print(f"Congrats {name} you guessed it correct '{ans}'")
            def ret():
                retry = input(f"{Fore.BLUE}Do you want to play again ?? yes or no ").upper()
                if retry == "YES":
                    games(lives)
                elif retry == "NO":
                    print(f"{Fore.YELLOW}Thank you kindly rate the game before you leave, Have a great day")
                    def rating():
                        rate = int(input(f"{Fore.YELLOW}Rate 1 to 5. 1 is lower and 5 is higher "))
                        if rate == 1:
                            print(f"{Fore.BLUE}We work harder to improve and match to your expectation")
                        elif rate == 2:
                            print(f"{Fore.BLUE}We are trying our best for better improvements")
                        elif rate == 3:
                            print(f"{Fore.BLUE}Hold on there we will reach you expectations soon")
                        elif rate == 4:
                            print(f"{Fore.BLUE}This is still not enough for us we make sure our user gets best out of best experience, we try even harder")
                        elif rate == 5:
                            print(f"{Fore.BLUE}Am glad you liked it")
                        else:
                            print(f"{Fore.RED}Please enter the valid number")
                            rating()
                    rating()
                else:
                    print(f"{Fore.RED}Please enter the valid keyword")
                    ret()
            ret()
        else:
            game = True


games(lives)
