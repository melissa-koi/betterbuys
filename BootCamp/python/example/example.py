# import sys
#
# name = sys.argv[1]
# print("How old are you?")
# age = int(input())
#
# print(name)
# print(age)

# height = 69
# if height > 70:
#     print("You are really tall")
# elif height > 60:
#     print("You are of average height")
# else:
#     print("You are really short")

# name = ""
# list_a = []
#
# if list_a:
#     print("True")
# else:
#     print("False")

# list_a = range(0, 5)
# print(list_a)

# for i in range(0, 7):
#     print("I would love " + str(i) + " cookies")

# numbers = [1, 2, 3, 4, 5]
# for i in numbers:
#     if i % 2 == 0:
#         print(i)

# players = 11
# while players >= 5:
#     print("The remaining players are ", players)
#     players -= 1

# number = 0
# while True:
#     print("I love candy " + str(number))
#     number += 1
#     if number == 7:
#         break

# numTaken = [3, 5, 7, 11, 13]
# print("Available Numbers")
#
# for i in range(1, 21):
#     if i in numTaken:
#         continue # or break
#     print(i)

# my_list = []
# my_other_list = list()
# list_a = ["a", "b", "c", "d"] # list of strings
# list_b = [1, 2, 3, 4, 5, 6] # list of numbers
# list_c = [1, "west", 34, "longitude"] # mixed list
# list_d = [ ["a","b","c","d"],[1,2,3,4,5,6],[1,"west",34,"longitude"]] # nested list
#
# list_a.extend(list_b)
# print(list_a)
# print(list_b)

# my_cat = {'name': 'Mr.Sniffles', 'age': 18, 'color': 'black'}
#
# print(my_cat['name'])
# print(my_cat)
#
# print(list(my_cat.keys()))

# print("Enter a string")
# input_string = input()
# characters = {}
#
# for character in input_string:
#     characters.setdefault(character, 0)
#     characters[character] = characters[character] + 1
#
# print(characters)

# print('What is your name?')
# name = input()
# print('How old are you?')
# age = input()
# print(f"My name is {name} and i am {age} years old")

# name = "James"
# age = 19
# weight = '79' # Kilograms
#
# age_weight_ratio = int(weight)/age
# age_weight_ratio2 = float(weight)/age
#
# print(age_weight_ratio)
# print(age_weight_ratio2)

def fun_a(a=1, b=4):
    print(a + b)
fun_a()

def fun_b():
    pass

def fun_c(a, b):
    return a + b
sum = fun_c(5, 8)
print(sum)
