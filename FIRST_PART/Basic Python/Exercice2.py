##
## EPITECH PROJECT, 2022
## workshop-scrapy
## File description:
## Exercice2
##


if __name__ == "__main__":
    if (len(argv) != 2):
        exit(84)
    number_list = list(argv[1])
    result_list = list()
    last_result = int(number_list[0])
    len_list = len(number_list)
    for i in range (len_list):
        result_list.append(int(number_list[i]))
        if (i + 1 != len_list):
            result_list.append(int(number_list[i]) * int(number_list[i + 1]))
        if (i != 0):
            last_result *= int(number_list[i])
    result_list.append(last_result)
    if(len(set(result_list)) == len(result_list)):
        print(argv[1] + " --> True")
    else:
        print(argv[1] + " --> False")
