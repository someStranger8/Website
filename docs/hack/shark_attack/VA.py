import random
import os
import time
import sys
def main():
    i=1
    while i < 10:
        god=input("ask me something >>> ")
        if god == "help":
            print("im POGGER ask me any thing")
            print("for more ask me what i can do")
        elif god == "what is the answer to life the universe and everything":
            print("42")
        elif god == "up up down down left right left right b a start":
            print("super gamer mode unlocked")
        elif god == "oh my god, they killed kenny":
            print("thoose basterds")
        elif god == "what can you do":
            print("heres what i can do: bully you, laugh at you, say cuss words, annihilate the world")
            print("heres what i cant do: solve a mystery with the mystery gang, bake a cake, be nice")
        elif god == "hello":
            print("hi im POGGER your virtual assistant")
        elif god == "python":
            os.system("python3")
        elif god == "shell":
            a=1
            while a < 10:
                dodo=input("dodo@dodo:~$ ")
                if dodo == "exit":
                    main()
                else:
                    os.system(dodo)
        elif god == "clear":
            os.system("clear")
        elif god == "exit":
            sys.exit()
        else:
            pacote = ["did you mean i would like to order a bomb gun","telling your folowers on twitter they can suck fat nards","did you mean i would like to nuke russia","sorry i did not catch that did you say your a terrorist","alexa is stupid and is dog shit but that is something you already know","can you shut the fuck up im tired of listening to you","god damn it why are you asking me go search it up on google jack ass",]
            game = random.choice(pacote)
            print(game)
    i+=1
main()
