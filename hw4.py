# Sem4

import random

# 1) Начало
def sum(listNumber):
    result = 0
    index = 0
    for i in listNumber:
        if (index % 2 != 0):
            result += i
        index += 1

    return result

# 1) Вывод
listNumber = [2,3,5,9,3]
print("1) " + str(sum(listNumber)))

# 1) Конец
# _________________________

# 2) Начало

def fillList(rowCount, columnCount):
    arrayOfNumbers = [[]] * rowCount

    for row in range(rowCount):
        arrayOfNumbers[row] = []
        for column in range(columnCount):
            arrayOfNumbers[row].append(random.randint(1, 9))
    return arrayOfNumbers


def getMidArifNumber(arr, rowCount, columnCount):
    for row in range(rowCount):
        midNumber = 0
        for column in range(columnCount):
            midNumber += arr[row][column]
        midNumber = midNumber / columnCount
        print(str(arr[row])+": " + str(midNumber))

# 2) Вывод
columnCount = int(input("Введите число колонок: "))
rowCount = int(input("Введите число строк: "))

arrayOfNumbers = fillList(rowCount, columnCount)
print("2) ")
getMidArifNumber(arrayOfNumbers, rowCount, columnCount)


# 2) Конец
# ____________________________

# 3) Начало

def getBigList (number):
    listNumbers = []
    for i in range(number):
        listNumbers.append(random.randint(1, 99))
    return  listNumbers


def sortBigList(listNumbersOld, number):
    listNumbersNew = listNumbersOld
    for i in range(number - 1):
        for j in range(number - i - 1):
            if listNumbersNew[j] > listNumbersNew[j + 1]:
                vremennoe = listNumbersNew[j]
                listNumbersNew[j] = listNumbersNew[j + 1]
                listNumbersNew[j + 1] = vremennoe
    return listNumbersNew

# 3) Вывод

listNumbers = getBigList(30)
print(listNumbers)

listNumbersNew = sortBigList(listNumbers, 30)
print(listNumbersNew)

# 3) Конец
# _________________________
