##
## EPITECH PROJECT, 2022
## workshop-scrapy
## File description:
## Exercice3
##

def calculate(myList):
    if isinstance(myList, list) == False:
        return False
    cpt = 0
    for i in myList:
        if ((isinstance(i, str)) and i.isnumeric()):
            cpt += int(i)
    print(cpt)

calculate(453)
    
    