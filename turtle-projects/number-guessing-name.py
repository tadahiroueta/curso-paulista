a1=('lol')
a2=0
nm=input('Hello. what´s ur name?')
gs=0
#input variation
print('Well,',nm,', I was thinking of a number from 1 to 100.Would u like to try to gues it?(Yes or No)')
a1=input(str())
#intruduction
import random
n=random.randint(1, 100)
#importation
if a1=='Yes'or a1=='yes':
    print('Ok then. What´s ur guess,',nm)
#acceptation of game
    while a2!=n:
        a2=int(input())
        if a2<n:
            print('Sorry, but that´s not big enough.')
        if a2>n:
            print('Sorry, but that´s too big.')
        if a2!=n:
            print('Try again.')
            gs=gs+1
#management of guesses
    print('Congrats. U got the number right, and it only took u',gs,'attemps!')
else:
    print('Ok then, if you don´t want to play.')
#ending
