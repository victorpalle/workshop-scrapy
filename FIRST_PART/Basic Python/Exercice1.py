##
## EPITECH PROJECT, 2022
## workshop-scrapy
## File description:
## Exercice1
##

def customPrint():
    for i in range (1, 101):
        if (i % 3 == 0) and (i % 5 == 0):
            print("ThreeFive")
        elif (i % 3) == 0:
            print("Three")
        elif (i % 5) == 0:
            print("Five")
        print(i)


customPrint()       
