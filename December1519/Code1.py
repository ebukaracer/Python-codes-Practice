#VALIDATION RULE
# name = input("Name: ")
#
# if len(name) < 3:
#     print('Name must atleast be less than 3 characters long')
#
# elif len(name) > 50:
#     print('Name can be a maximum of 50 characters')
#
# else:
#     print('Name looks good!')

#WEIGHT CONVERTER
# weight = int(input('Weight: '))
#
# Unit = input('K(kgs) or L(pbs)').lower()
#
# if Unit == 'k':
#     converted_weight = weight * 0.45
#     print(f'You are {converted_weight} kilos')
#
# else:
#     converted_weight = weight / 0.45
#     print(f'You are {converted_weight} pounds')
#

# WHILE LOOPs
# i = 0
#
# while i < 5:
#     print(i)
#     print('Ebuka')
#     i += 1
# print('Done!')
#

# GUESSING GAME
# secret_number = 9
# number_of_guesses = 3
# guess_count = 1
#
# while guess_count <= number_of_guesses:
#
#     guess_num = int(input('Guess: '))
#
#     if guess_num != secret_number:
#         guess_count += 1
#
#     else:
#         print(f'{guess_num}, You win!')
#         break
#
# else:
#     print('You Loose')

#CAR GAME
# command = ""
# car_started = False
#
# while True:  # or #command != "Quit":
#     command = input('> ')
#
#     if command == 'help':
#         print("""
#
# start - start car
# stop - stop car
# quit - exit
#
#         """)
#
#     elif command == 'start':
#         if not car_started:
#             print('car started, ready to go!')
#             car_started = True
#         else:
#             print('Car already started')
#
#     elif command == 'stop':
#         if not car_started:
#             print('Car already stopped')
#         else:
#             print('car stopped')
#             car_started = False
#
#     elif command == 'quit':
#         break
#
#     else:
#         print('Sorry, try again!')

#Sum of numbers in a list
# sum = 0
# for x in (10, 20, 30):
#     sum += x
# print(sum)

#max number in a list
# numbers = [20, 50, 70, 30, 120, 60]
# Max = numbers[0]
# for number in numbers:
#     if number < Max:
#         Max = number
# print(Max)

#forLoops
    # for x_output in range(x_count):
    #     output += '*'
    # print(output)
    #

# matrix =[
#
#     [1, 2, 5],
#     [3, 6, 10],
#     [1, 5, 9]
#
# ]
#
# matrix.insert(2, [8, 6, 8])
# for matrixes in matrix:
#     for innermatrix in matrixes:
#         print(innermatrix)
#

# numbers = [2, 4, 6, 2, 5]
# duplicate = []
# for n in numbers:
#     if n not in duplicate:
#         duplicate.append(n)
# print(duplicate)

#inner loops
# for x in range(3):
#     for y in range(4):
#         print(f'(x:{x}, y:{y})')

#unpacking
# cordinates = (1, 2, 3)
# x, y, z = cordinates
# ans = x*y*z
# print(ans)

#dictionaries
# customer = {
#     "name":'ebuka',
#     "age":17,
#     "height":160
# }
#
# customer["name"] = "racer"
# print(customer["name"])

# inp = input(">: ")
#
# customer = {
#     "r":"R",
#     "a":"A",
#     "c":"C",
#     "e":"E",
#     "r":"R"
# }
#
# output = ''
# for user in inp:
#     output += customer.get(user, "null") + " "
# print(output)


# message = input('> ')
# letters = message.split(' ')
# translation = {
#     "happy": "HAPPY",
#     "sad": "SAD"
# }
#
# output = ''
# for words in letters:
#     output += translation.get(words, words) + " "
#     #output += translation[words]
#
# print(output)
#
# def message(name, age, height):
#     print(f'Hello world! my name is {name}, i am {age} old and {height}cm tall')
#     print('Thank you!')
#
#
# name = input('> ')
# age = int(input('> '))
# height = int(input('> '))
#
# message(name, age, height)

# def sqr(number):
#     return number * number
#     #print(number * number)
#
#
# print(sqr(3))


# def emoji_converter(message):
#     letters = message.split(' ')
#     translation = {
#          "happy": "HAPPY",
#          "sad": "SAD"
#     }
#
#     output = ''
#     for words in letters:
#         output += translation.get(words, words) + " "
#         #output += translation[words]
#     return output
#
#
# message = input('> ')
# print(emoji_converter(message))

# try:
#
#     no1 = int(input('Enter 1st no: '))
#     no2 = int(input('Enter 2nd no: '))
#
#     solution = no1 / no2
#
#     print(f'Answer: {solution}.')
#
# except ValueError:
#     print('INVALID, Enter a numerical value')


# def calculator(no1, no2, sign):
#     if sign == '+':
#         answer = no1 + no2
#         return f'Answer: {answer}'
#
#     elif sign == '-':
#         answer = no1 - no2
#         return f'Answer: {answer}'
#
#     elif sign == '/':
#         answer = no1 / no2
#         return f'Answer: {answer}'
#
#         return 'INVALID SIGN!'
#
#
# no1 = int(input('Enter 1st no: '))
# sign = input('Enter sign: ')
# no2 = int(input('Enter 2nd no: '))
#
# print(calculator(no1, no2, sign))

"#use return, print out the declared function, use print inside the method, leave out printing the function"""


# class Point:
#     def move(self):
#         return 'Move'
#
#     def draw(self):
#         return 'draw'
#
#
# point1 = Point()
# point1.x = 2
# point1.y = 3
# print(point1.draw())

# class Person:
#
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def output(self):
#         print(f'Answer = {self.x + self.y + self.z}')
#
#
# addition = Person(10, 20, 30)
#
# addition.output()

# class Mammal:
#     def walk(self):
#         print('Mammals walk')
#
#     def fly(self):
#         print('some mammals fly')
#
#     def birth(self):
#         print('Mammals reproduce')
#
#
# class Dog(Mammal):
#     def bark(self):
#         print('Dogs bark')
#
#     def pet(self):
#         print('Dogs are home pets')
#
#
# first_animal = Dog()
#
# first_animal.bark()
# first_animal.birth()
# first_animal.pet()
# first_animal.walk()

import utils

# from utils import find_max
#
# numbers = [2, 4, 6, 2, 5]
# print(find_max(numbers))


#print(utils.find_max())

# Numbers = (input("Enter Numbers > "))
#
# main_numbers = Numbers.split(',')

user = input('Type (start) to start or (quit) to exit> ').lower()
List = []
while user != 'quit':
    Numbers = int(input("Enter Numbers: "))

    List.append(Numbers)

    if len(List) >= 5:
        break

smallest = []

while len(smallest) < 3:

    min_list = List[0]
    for lists in List:

        if min_list > lists:
            min_list = lists

    smallest.append(min_list)
    List.remove(min_list)


print('The three smallest numbers in your lists are: ')
for new_list in smallest:
    print(new_list)


