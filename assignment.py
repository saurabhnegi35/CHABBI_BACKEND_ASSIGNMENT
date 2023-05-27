# Q1. Get your basics right - Implement selection sort algorithm in python. The function accepts a
# list in the input and returns a sorted list.
# E.g.
# Input f1([5,416,54,21,6135,15,741]) should
# Return [5, 15, 21, 54, 416, 741, 6135]


def selectionSort(lst):
    for i in range(len(lst)):
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst

inputList = input("Enter a list of numbers (space-separated): ").split()
inputList = [int(num) for num in inputList]

sortedList = selectionSort(inputList)

print("Sorted List:", sortedList)




# Q2. Dictionary, what?
# Write a program that returns the file type from a file name. The type of the file is determined
# from the extension. Initially, a list of values of the form "extension,type"(e.g. xls,spreadsheet;
# png,image) will be input.
# The program takes input in the following form:
# 1. Input extension and type values in the form of a string having the following format:
# a. "extension1,type1;extension2,type2;extension3,type3"
# b. E.g. If we needed to input xls → spreadsheet, xlsx → spreadsheet, jpg → image
# our string would be something like: "xls,spreadsheet;xlsx,spreadsheet;jpg,image"
# 2. Input a list of filename.extension. E.g. an input list could be something like ["abc.html",
# "xyz.xls", "text.csv", "123"]
# The program should return a dict of filename: type pairs
# E.g.
# f("xls,spreadsheet;xlsx,spreadsheet;jpg,image", ["abc.jpg",
# "xyz.xls", "text.csv", "123"]) should return
# {
# "abc.jpg": "image",
# "xyz.xls": "spreadsheet",
# "Text.csv": "unknown",
# "123": "unknown"
# }

def getFileTypes(extensionTypeString, fileList):
    fileTypes = {}
    extensionTypePairs = extensionTypeString.split(';')

    exteextensionDict = {}
    for pair in extensionTypePairs:
        extension, fileType = pair.split(',')
        exteextensionDict[extension] = fileType

    for file in fileList:
        
        parts = file.split('.')
        if len(parts) > 1:
            extension = parts[-1]
        else:
            extension = ""

        fileType = exteextensionDict.get(extension, "unknown")
        fileTypes[file] = fileType

    return fileTypes

extensionTypeString = "xls,spreadsheet;xlsx,spreadsheet;jpg,image"
fileList = ["abc.jpg", "xyz.xls", "text.csv", "123"]

result = getFileTypes(extensionTypeString, fileList)
print(result)




# Q3. Column Sorting, yay!

# Given a list of dicts, write a program to sort the list according to a key given in input.
# E.g.
# Input f([
# {"fruit": "orange", "color": "orange"},
# {"fruit": "apple", "color": "red"},
# {"fruit": "banana", "color": "yellow"},
# {"fruit": "blueberry", "color": "blue"}
# ], "fruit")
# Should Output
# [
# {"fruit": "apple", "color": "red"},
# {"fruit": "banana", "color": "yellow"},
# {"fruit": "blueberry", "color": "blue"},
# {"fruit": "orange", "color": "orange"}
# ]
# AND
# Input f([
# {"fruit": "orange", "color": "orange"},
# {"fruit": "apple", "color": "red"},
# {"fruit": "banana", "color": "yellow"},
# {"fruit": "blueberry", "color": "blue"}
# ], "color")
# Should Output
# [
# {"fruit": "blueberry", "color": "blue"},
# {"fruit": "orange", "color": "orange"},
# {"fruit": "apple", "color": "red"},
# {"fruit": "banana", "color": "yellow"}
# ]

def f(lst, key):
    return sorted(lst, key=lambda x: x[key])

data = [
    {"fruit": "orange", "color": "orange"},
    {"fruit": "apple", "color": "red"},
    {"fruit": "banana", "color": "yellow"},
    {"fruit": "blueberry", "color": "blue"}
]

sortedData = f(data, "fruit")
print(sortedData)

sortedData = f(data, "color")
print(sortedData)


# Q4. The power of one line -
# Given a dictionary, switch position of key and values in the dict, i.e., value becomes the key and
# key becomes value. The function's body shouldn't have more than one statement.
# f({
# "key1": "value1",
# "key2": "value2",
# "key3": "value3",
# "key4": "value4",
# "key5": "value5"
# }) should return
# {
# "value1": "key1",
# "value2": "key2",
# "value3": "key3",
# "value4": "key4",
# "value5": "key5"
# }

def switchKeyValue(dictionary):
    return {v: k for k, v in dictionary.items()}

originalDict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    "key4": "value4",
    "key5": "value5"
}

switchedDict = switchKeyValue(originalDict)
print(switchedDict)


# Q5. Common, Not Common
# Given 2 lists in input. Write a program to return the elements, which are common to both
# lists(set intersection) and those which are not common(set symmetric difference) between the
# lists.
# Input:
# Mainstream = ["One Punch Man","Attack On Titan","One Piece","Sword
# Art Online","Bleach","Dragon Ball Z","One Piece"]
# mustWatch = ["Full Metal Alchemist","Code Geass","Death
# Note","Stein's Gate","The Devil is a Part Timer!","One Piece","Attack
# On Titan"]
# f(mainstream, mustWatch) should return:
# ["One Piece", "Attack On Titan"], ["Dragon Ball Z", "Death Note",
# "One Punch Man", "Stein's Gate", "The Devil is a Part Timer!", "Sword
# Art Online","Full Metal Alchemist","'Bleach", "Code Geass"]

def compareLists(list1, list2):
    commonElements = list(set(list1) & set(list2))
    notCommonElements = list(set(list1) ^ set(list2))
    return commonElements, notCommonElements

mainstream = [
    "One Punch Man", "Attack On Titan", "One Piece", "Sword Art Online",
    "Bleach", "Dragon Ball Z", "One Piece"
]
mustWatch = [
    "Full Metal Alchemist", "Code Geass", "Death Note", "Stein's Gate",
    "The Devil is a Part Timer!", "One Piece", "Attack On Titan"
]

common, notCommon = compareLists(mainstream, mustWatch)
print(common)
print(notCommon)


# Q6. Every other sub-list
# Given a list and 2 indices as input, return the sub-list enclosed within these 2 indices. It should
# contain every second element.
# E.g.
# Input f([2,3,5,7,11,13,17,19,23,29,31,37,41], 2, 9)
# Return [5, 11, 17, 23]

def getEveryOtherSublist(lst, startIdx, endIdx):
    subList = lst[startIdx:endIdx+1:2]
    return subList

numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
startIndex = 2
endIndex = 9

result = getEveryOtherSublist(numbers, startIndex, endIndex)
print(result)


# Q7. Calculate the factorial of a number using lambda function.


from functools import reduce

def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))

number = 5
result = factorial(number)
print(result)



# Q8. Some neat tricks up her sleeve:
# Looking at the below code, write down the final values of A0, A1, ...An
# A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
# A1 = range(10)
# A2 = sorted([i for i in A1 if i in A0])
# A3 = sorted([A0[s] for s in A0])
# A4 = [i for i in A1 if i in A3]
# A5 = {i:i*i for i in A1}
# A6 = [[i,i*i] for i in A1]
# A7 = reduce(lambda x,y: x+y, [10,23, -45, 33])
# A8 = map(lambda x: x*2, [1,2,3,4])
# A9 = filter(lambda x: len(x) >3, [“I” , “want”, “to”, “learn”, “python”])


A0 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
A1 = range(0, 10)
A2 = [1, 2, 3, 4, 5]
A3 = [1, 2, 3, 4, 5]
A4 = [1, 2, 3, 4, 5]
A5 = {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
A6 = [[0, 0], [1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49], [8, 64], [9, 81]]
A7 = 21
A8 = <map object at 0x000001234567890>
A9 = <filter object at 0x000001234567890>



# Q9.
# Write a func that takes 3 args:
# from_date - string representing a date in the form of 'yy-mm-dd'
# to_date - string representing a date in the form of 'yy-mm-dd'
# difference - int
# Returns True if from_date and to_date are less than difference days away from each other, else
# returns False.

from datetime import datetime, timedelta

def dateDifferenceLessThan(from_date, to_date, difference):
    date_format = '%y-%m-%d'
    date1 = datetime.strptime(from_date, date_format)
    date2 = datetime.strptime(to_date, date_format)
    delta = abs(date2 - date1)
    return delta.days < difference

from_date = '21-05-10'
to_date = '21-04-05'
difference = 10

result = dateDifferenceLessThan(from_date, to_date, difference)
print(result)


# Q10. Of date and days
# Write a func that takes 2 args:
# date - string representing a date in the form of 'yy-mm-dd'
# n - integer
# Returns the string representation of date n days before 'date'
# E.g. f('16-12-10', 11) should return '16-11-29'
# Q11. Something fishy there -
# Find output of following:
# def f(x,l=[]):
# for i in range(x):
# l.append(i*i)
# print(l)
# f(2)
# f(3,[3,2,1])
# f(3)


from datetime import datetime, timedelta

def getDateBefore(date, n):
    date_format = '%y-%m-%d'
    given_date = datetime.strptime(date, date_format)
    new_date = given_date - timedelta(days=n)
    return new_date.strftime(date_format)

date = '16-12-10'
n = 11

result = getDateBefore(date, n)
print(result)