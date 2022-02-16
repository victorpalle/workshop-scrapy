##
## EPITECH PROJECT, 2022
## workshop-scrapy
## File description:
## Execrice4
##

def areAnagram(str1, str2):
    n1 = len(str1)
    n2 = len(str2)
 
    if n1 != n2:
        return 0
 
    str1 = sorted(str1)
    str2 = sorted(str2)
 
    for i in range(0, n1):
        if str1[i] != str2[i]:
            return 0
    return 1
 



def anagrams(single, myList):
    tmp = []
    for string in myList:
        if areAnagram(single, string):
            tmp.append(string)
    print(tmp)
            


anagrams('abba', ['abba', 'baba'])