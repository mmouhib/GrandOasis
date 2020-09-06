import os
import random
import sys
import ctypes
import random
from termcolor import colored
from datetime import datetime

os.system('cls')

start_time = datetime.now()


def TimeCalc(start_time):
    end_time = datetime.now()
    ch = str(end_time - start_time)
    hrs = ch[0:1]
    mnt = ch[2:4]
    sec = ch[5:7]
    printer(2)
    if hrs == '0' and mnt == '00':
        print(colored("you've spent "+sec+" seconds on this run.", 'red'))
    elif hrs == '0':
        print(colored("you've spent "+mnt+" minutes and " +
                      sec+" seconds on this run.", 'red'))
    else:
        print(colored("you've spent "+hrs+" hours and "+mnt +
                      " minutes and "+sec+" seconds on this run.", 'red'))


# C:\dev\python3\rpg.py
def printer(x):
    for i in range(0, x):
        print()


def clrscr():
    rep = input('Press ENTER to continue'.center(120))
    if rep == '':
        os.system('cls')
        print()
        print()
        print()


def welcome():
    printer(2)
    print(colored("◘ Welcomed To 'Grand Oasis' ◘ ", 'magenta').center(120))
    printer(3)


def playername():
    name = ''
    while name == '':
        name = input('Pick A user Name: ')
    printer(3)
    return name


def difficulty():
    printer(3)
    print(colored('1- EASY', 'green').center(140))
    printer(1)
    print(colored('2- MEDIUM', 'green').center(140))
    printer(1)
    print(colored('3- HARD', 'green').center(140))
    printer(2)
    choice = '0'
    while choice != '1' and choice != '2' and choice != '3':
        choice = input('choose your difficulty (<1/2/3>) :  ')
    return choice


def difficulty2(choice):
    printer(2)
    if choice == '1':
        print("""hmmm, seems like you are here just for the plot,
that's fine but we're looking for a real Warrior here """)
    elif choice == '2':
        print("Not bad, but try to dream bigger next time")
    else:
        print('Nice, Go HARD or go HOME, huh?')
    printer(4)


def FirstPrintStats(health, ehealth):
    print('** You have ' + str(health)+'HP **')
    print('** Your Enemy has ' + str(ehealth)+'HP **')
    print()
    print(colored('1- Hit Enemy', 'blue'))
    print(colored('2- Drink a potion', 'red'))
    print(colored('3- Run away', 'blue'))
    print(colored('4- Use your Super curse', 'red'))
    printer(3)


def FirstChoiceMaking():
    choice = '0'
    while choice != '1' and choice != '3':
        choice = (
            input('Make Your Choice => (!! *red options are not available yet !!) '))
    os.system('cls')
    return int(choice)


def StoryOne(name):
    clrscr()
    print("""once upon a time in a place far far from earth deep down in the ground

there was a princess that was not found for weeks and all the people were looking for her

And one day when her prince was doing what he does everyday since his princess was lost

and it is looking for her everywhere in the kingdom

he found a message written on a tree in the forest and it said:

'HELP ME, the Dark Minister's soldiers kidnapped me'

		""")

    printer(3)
    clrscr()
    print("you might be thinking what is the name of the prince, huh ")
    phrase = "his name is " + name
    printer(3)
    print(phrase.center(110))
    printer(3)
    print("now you're back to the castle to prepare for your long journey of helping your princess")
    print("You'll get to choose your preset in the next few seconds")
    printer(6)
    clrscr()


def ClassPicking():
    print(colored('1- Armoder Warrior ', 'green').center(120))
    print("This preset lets you deal less damage but also receive less.".center(110))
    printer(2)
    print(colored('2- light Warrior  ', 'green').center(120))
    print("This preset lets you receive more damage but also deal more.".center(110))
    printer(2)
    print(colored('3- Stealth Ghost  ', 'green').center(120))
    print("This preset has the ability deal a massive amount of damage but,".center(110))
    print("you might fail your shots and deal a little to nothing damage.".center(110))
    printer(7)
    choice = '0'
    while choice != '1' and choice != '2' and choice != '3':
        choice = input("pick a Class: (<1/2/3>) ")
    return choice


def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)


def FirstCombat(diff, cat):
    if diff == '1':
        health = 200
        ehealth = 160
    elif diff == '2':
        ehealth = health = 150
    else:
        health = 100
        ehealth = 120
    FirstPrintStats(health, ehealth)
    while health > 0 and ehealth > 0:
        chs = FirstChoiceMaking()
        if chs == '3':
            health = 0
        if chs == 1:
            if cat == '1':
                if diff == '1':
                    hit = random.randint(19, 40)
                    ehit = random.randint(14, 30)
                elif diff == '2':
                    hit = random.randint(19, 40)
                    ehit = random.randint(29, 40)
                else:
                    hit = random.randint(9, 25)
                    ehit = random.randint(14, 30)
            elif cat == '2':
                if diff == '1':
                    hit = random.randint(29, 50)
                    ehit = random.randint(24, 40)
                elif diff == '2':
                    hit = random.randint(29, 50)
                    ehit = random.randint(29, 50)
                else:
                    hit = random.randint(19, 35)
                    ehit = random.randint(24, 40)
            else:
                x = random.randint(0, 2)
                if x == 1:
                    if diff == '1':
                        hit = random.randint(29, 50)
                        ehit = random.randint(24, 40)
                    elif diff == '2':
                        hit = random.randint(29, 50)
                        ehit = random.randint(29, 50)
                    else:
                        hit = random.randint(19, 35)
                        ehit = random.randint(24, 40)
                else:
                    if diff == '1':
                        hit = random.randint(9, 15)
                        ehit = random.randint(24, 40)
                    elif diff == '2':
                        hit = random.randint(9, 15)
                        ehit = random.randint(29, 50)
                    else:
                        hit = random.randint(9, 15)
                        ehit = random.randint(24, 40)
            health -= ehit
            ehealth -= hit
            if health < 0:
                health = 0
            if ehealth < 0:
                ehealth = 0
            FirstPrintStats(health, ehealth)
    if ehealth > health:
        print("Unfortunately you've lost ")
        return 0
    if health > ehealth:
        print("Congrats, you have won the battle ")
        printer(4)
        return 1
    else:
        return 2


def StoryTwo():
    printer(6)
    print("On your way To the forest to look for where to find any traces of the Dark Minister's army,")
    print("a monter showed up")
    printer(7)


def StoryThree():
    print("""After defeating the monster, an old man showed up and said:

-looks like you are a though man, and a fearless one too to come here to this cursed land owned by the Dark Minister

what brings you here young man ?


	""")

    print(colored('1- None of your business old man', 'blue'))
    print(colored('2- I came here looking for my princess she was kidnapped', 'blue'))
    print(colored("3- You said 'cursed' !,  how is that ?!", 'blue'))
    printer(2)

    choice = '0'
    while choice != '1' and choice != '2' and choice != '3':
        choice = input('choose what you want to say (<1/2/3>) :  ')
    if choice == '1':
        os.system('cls')
        printer(5)
        print("""Okay Young man you've chosen death
and the old man transforms into a huge monster and cuts your guts with his sharp hands

                       !! next time try to be nicer to elders !!

		""")

        return False
    elif choice == '2':
        printer(5)
        print("hmm, seems like she was taken by the Dark Minister")
        print("you can't cross his land and expect to go back where you came from without passing 'The Darkness Tests' ")
        printer(4)
        clrscr()
        printer(3)
        print(colored('1- Okay thanx for your help', 'blue'))
        print(colored("2-'The Darkness Tests' ?!, what are THOSE", 'blue'))
        printer(5)
        choice = '0'
        while choice != '1' and choice != '2':
            choice = input('choose what you want to say (<1/2/3>) :  ')
        if choice == '2':
            print("yeah my son, 'The Darkness Tests' it's a collection of tests and puzzles you have to pass to beat the Dark Minister")
            print("you think that you'll have to fight him to beat him, he just can blow on your face and push you back 100 Kilometers")
            printer(5)
        else:
            os.system('cls')
            printer(6)
            print("Be carefoul out there my son, it's a long journey !")
            printer(3)
        return True

    else:
        os.system('cls')
        print("Yes my son, this forest is cursed and it is owned by the Dark Minister and his followers")
        print("any you may wonder how am i here and still alive and kicking ")
        print("let me tell you a story: ")
        printer(5)
        clrscr()
        print("""96 years ago when i was 7 year old when i spent the happiest 7 years of my life,

this place was the most beautiful area in the whole world

there were beautiful trees and flowers with a lot of colors and animals and people living in peace

until one day a curious little kid went to a place that no one talked about in the forest

it was a small dungeon and a little square like a grave, and there was a key help into it

that kid made the biggest fault by spinning the key and releasing the Dark Minister  who was

prisonned by i suppose your grandmother's grandfather the King of Kings 'Norman'

since then, the Dark Minister took over and killed everyone in this place
		""")
        printer(8)
        clrscr()
        return True
        print(colored('1- but why are you still alive', 'blue'))
        print(colored("2- oh! ,that's so sad", 'blue'))

        while choice != '1' and choice != '2':
            choice = input('choose what you want to say (<1/2/3>) :  ')
        if choice == '1':
            print("- Yeah i forgot to tell you i was the Kid who unleashed the Demon and he spared me because i released him")
        else:
            print("yeah it is, ALEXA play DESPACITO")
        clrscr()

        print("""listen here little warrior, the path that you're taking is very tough so be carefoul

here is a magical drink that can help you in some fights againts the enemies by restoring some of your health

be carefoul and try not to die

...

wait, i forgot to tell you, if you manage to pass the 'Darkness Tests' you are able to rescue all the prisoners

including your princess
	
			""")


def PrintGameOver():
    printer(3)
    print("GAME OVER!".center(150))
    Mbox(':(', "GAME OVER! Better luch next time", 1)
    printer(2)
    TimeCalc(start_time)
    printer(3)
    requestcredits()
    last()


def PreStoryFour():
    print("you advance in and reach the Gate of the Dark Minister's castle")
    printer(2)
    print("Carefoul, two enemies on the door")
    print()


def StoryFour(diff, ch):
    if ch == 'Third':
        print()
        print("Another enemy coming")
        print()
    if diff == '1':
        health = 200
    elif diff == '2':
        health = 150
    else:
        health = 100
    FirstPrintStats(health, 10)
    choice = '0'
    while choice != '1' and choice != '3':
        choice = input(
            "choose what to do (<1/3>) (options in red are not available yet):  ")
    if choice == '1':
        os.system('cls')
        FirstPrintStats(health, 0)
        Mbox('Conngrats', "You have slain your "+ch+" enemy !", 1)
    return choice


def StoryFive():
    print("""you enter the Castle, it is dark and nasty

you see symbols that leads to the cave where all the prisoners are including your princess

You see her and try to touch her hand but a big lighting comes out and you find yourself teleported to a big place full of nothing

the Dark Minister comes out and says

- Hello friend

	""")

    printer(3)
    print(colored(" 1- < Jump and try to Slay him with your sword >", 'blue'))
    print(colored(" 2-'I am not your friend' ", 'blue'))
    printer(2)
    choice = '0'
    while choice != '1' and choice != '2':
        choice = input("choose what to do (<1/2/3>) :  ")
    if choice == '1':
        os.system('cls')
        print("you made the wrong choice son ")
        print("Die now,")
        PrintGameOver()
        return False
    elif choice == '2':
        printer(3)
        clrscr()
        print("""Well, technicalley i can't be your friend because i was going to be your father if it wasn't for your grandfather's selfishness

ou reply: 
-wh.. wh.. what are you saying ?!

-Come here son, let me tell you a story again..

-Again ?!

-Oh, you didn't figure out that i was that old man who gave you the health potion before

look, i was one of your grandfather's soldiers a long time ago

i fell in love with his daughter, who is you mother

and we were gonna get married

		""")
        printer(3)
        clrscr()

        print("""and i had a big place in the kingdom and the people loved me because i was a good leader and cared about them

But you grandfather did not like that

and one day father, who was his right hand by that time, told him that i was preparing for a rebellion to kill him and take his place

so he cursed me and prisoned me in that grave that i've told you about before

and you father married your mother

such a happy ending, HUH?



Now i want to have vengence and take back what was before taken from me

and the only way to stop me from destroying your kingdom and releasing Darkness on the world,

you'll have to pass my 'Darkness Tests' before

it is a list of challenges that you have to pass

		""")
        printer(2)
        clrscr()
        return True


def TicTacToe():

    field = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    sbl1 = ''
    while(sbl1.upper() not in ('X', 'O')):
        sbl1 = input(" « PLAYER 1, Pick a symbol ('X' or 'O') » ")
        print()
    sbl1 = sbl1.upper()

    if sbl1 == 'X':
        sbl2 = 'O'
    else:
        sbl2 = 'X'

    def aff(list):
        print('--------- ')
        print(list[0]+' | '+list[1]+' | '+list[2]+'')
        print('--------- ')
        print(list[3]+' | '+list[4]+' | '+list[5]+'')
        print('--------- ')
        print(list[6]+' | '+list[7]+' | '+list[8]+'')
        print('--------- ')
        print()

    def FieldIsFull(list):
        v = True
        for i in list:
            if (i <= '9' and i >= '1'):
                v = False
                break
        return v

    def winner(t, sbl):
        if t[2] == t[4] == t[6] == sbl:
            return True
        elif t[0] == t[3] == t[6] == sbl:
            return True
        elif t[2] == t[5] == t[8] == sbl:
            return True
        elif t[1] == t[4] == t[7] == sbl:
            return True
        elif t[0] == t[4] == t[8] == sbl:
            return True
        elif t[0] == t[1] == t[2] == sbl:
            return True
        elif t[3] == t[4] == t[5] == sbl:
            return True
        elif t[6] == t[7] == t[8] == sbl:
            return True
        else:
            return False

    def testexistance(t, x):
        v = True
        for i in t:
            if i == x:
                v = False
                break
        return v

    field = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    gameover = False
    while gameover == False:
        aff(field)
        # getting the input of the indices
        if gameover == False:
            p1choice = ''
            while(p1choice == '') or (testexistance(field, p1choice)) or (p1choice > '9' and p1choice < '1'):
                p1choice = input(
                    'PLAYER 1, Choose one of the given Numbers inside the table ^^ ')
                print()
            field[int(p1choice)-1] = sbl1
        os.system('cls')
        aff(field)

        if winner(field, sbl1):
            gameover = True
            return '1'

        if not winner(field, sbl1) and FieldIsFull(field):
            gameover = True
            return '0'

        if gameover == False:
            x = random.randint(0, 8)
            field[x] = sbl2
            while not testexistance(field, x):
                x = random.randint(1, 9)
            field[x] = sbl2

        os.system('cls')
        if not winner(field, sbl2) and FieldIsFull(field):
            gameover = True
            return '0'

        if winner(field, sbl2):
            gameover = True
            return '2'


def clf():
    # NB of rounds
    printer(4)
    print("Welcome To 'CLF (frouda / zwez)'".center(120))
    rounds = 0
    printer(4)
    while(rounds == 0) or (int(rounds) % 2 == 0):
        rounds = int(input("How many Rounds do you wanna play ? "))
        print()
    print()

    # Player class (frouda/zwez) (Frouda Means an odd number and Zwez is the opposite)
    choice = ""
    while (choice != 'F') and (choice != "Z"):
        choice = input(
            "Choose 'F'/'Z' (frouda or zwez) (Frouda Means an odd number and Zwez is the opposite) ").upper()
        printer(5)

    pchoice = choice

    # PC class (froud/zwez) (Frouda Means an odd number and Zwez is the opposite)
    if pchoice == 'F':
        cchoice = 'Z'
    else:
        cchoice = 'F'

    clrscr()

    scorep = scorec = 0
    for i in range(0, rounds):
        pickp = 6
        while pickp not in range(0, 6):
            pickp = int(input('Pick a number between 1 and 5: '))
        pickc = random.randint(0, 5)
        print()
        pickcreplica = str(pickc)
        print("the PC has chosen: "+pickcreplica)
        print()
        total = pickp+pickc
        if pchoice == 'F':
            if total % 2 == 0:
                scorec += 1
            else:
                scorep += 1
        else:
            if total % 2 == 0:
                scorep += 1
            else:
                scorec += 1
        print('total: ' + str(total))
        print('player score: ' + str(scorep))
        print('coputer score: ' + str(scorec))
        print()
        print()
        print()
        print()
    if scorec > scorep:
        return False
    else:
        return True


def lastDialogue():
    print("""so i guess you are pretty decent here, but still

you don't have enough power to defeat me

let's proceed to the second test
    """)


def lastDialogue2():
    print("""ooh, you have some skills huh,

but still you'll have to beat me at all the challenges to shut me down

so let's proceed to the final test

    """)


def FinalDialogue():
    print("""Hmm, looks like you got me,

listen here little man, after this you'll become the king of the world

you'll have the ability to do whatever you want, kill whoever you want, 

so promise me that you'll be a good king and never harm anyone just because you think that you have the right to do

your power and place will be how you protect your kingdom not how to distroy it.
    
                        Goodbyes.    
    """)


def printmsg():
    print("""and the Dark Minister fades into the air,

and you are back when you found your princess, you rescue her and go back to the castle 
                                
    """)


def credits():
    print("""




                             ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥ 
                             ♥    this game was made by MOUHIB   ♥
                             ♥        started on 03/09/2020      ♥
                             ♥     was finished on 06/09/2020    ♥
                             ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
    
    
    
    
    """)


def requestcredits():
    clrscr()
    choice = '0'
    while choice != 'y' and choice != 'n':
        print(
            "Do you wanna see the credits [type 'y' for YES and 'n' for NO] ")
        choice = input("=> ")
    if choice == 'y':
        os.system('cls')
        credits()


def endgame():
    printer(3)
    print("Good job you've beaten the game!".center(125))
    Mbox(':(', "GGs! That was awesome", 1)
    printer(2)
    print("you spent:")
    TimeCalc(start_time)
    print("On this Run")
    requestcredits()
    last()


def last():
    clrscr()
    # os.system('cls')
    choice = '1'
    while choice != '':
        print("press ENTER to exit")
        choice = input("=> ")
    if choice == '':
        os.system('exit')


##callers##
welcome()
name = playername()
clrscr()
diff = difficulty()
difficulty2(diff)
StoryOne(name)
cat = ClassPicking()
printer(5)
clrscr()
StoryTwo()
clrscr()
win = FirstCombat(diff, cat)
scorep = scoree = 0
if win == 1:
    Mbox('Conngrats', "you have slain your first enemy !", 1)
elif win == 0:
    Mbox('Unfortunately', "You are DEAD !", 1)
else:
    Mbox('DRAW!', "You are Both Dead !", 1)

if win == 0 or win == 2:
    os.system('cls')
    PrintGameOver()
else:
    clrscr()
    v = StoryThree()
    if v == False:
        PrintGameOver()
    else:
        potion = 1
        clrscr()
        PreStoryFour()
        var11 = StoryFour(diff, 'Second')
        clrscr()
        if var11 == '1':
            print("Second enemy".center(140))
            print()
            var1 = StoryFour(diff, 'Third')
        else:
            os.system('cls')
            PrintGameOver()
        if var1 == '3':
            os.system('cls')
            PrintGameOver()
        else:
            clrscr()
            vv = StoryFive()
            if vv == False:
                PrintGameOver()
            else:
                xo = TicTacToe()
                if(xo == '2'):
                    Mbox('unfortunately', "You have lost to the dark minister !", 1)
                    PrintGameOver()
                elif xo == '1' or xo == '0':
                    if xo == '1':
                        scorep += 1
                        Mbox('Conngrats', "You have won the First challenge !", 1)
                        print("nice you've won")
                        printer(7)
                        scoree += 1
                    else:
                        print('DRAW !')
                        Mbox('Boring!', "it's a tie !", 1)
                        TimeCalc(start_time)
                    clrscr()
                    lastDialogue()
                    printer(5)
                    clrscr()
                    vvv = clf()
                    clrscr()
                    if vvv == False:
                        PrintGameOver()
                    else:
                        Mbox('Conngrats', "You have won the Second challenge !", 1)
                        lastDialogue2()
                        clrscr()
                        FinalDialogue()
                        printmsg()
                        clrscr()
                        endgame()
