print('Hello\nWorld\non multiple\nlines.')

y=3
x=+y
print(x)

# Exercise one Raise one number to the power of another number
print('\nExercise one Raise one number to the power of another number\n')
number = 5
toThePower = 10

print(pow(number,toThePower))

# Exercise two arrays
print('\nExercise two arrays\n')

import numpy as nparray

List4 = [[2,9,-5],[-1,0,4],[3,1,2]]
print(List4[0])
print(List4[1])
print('This is the value of second row in List 4 :' + str(List4[2]))
print('This is the value of the second cell on the second row in List 4 :' + str(List4[1][1]))
print("This is the mean of List4 :" + str(nparray.mean(List4)))

# Exersise three Check if number is divisable by three
print('\nExersise three Check if number is divisable by three\n')

number = 10
if number % 3 == 0:
    print(str(number) + ' is divisable by 3')
else:
        print(str(number) + ' is not divisable by 3')


# Exercise four Factorial of a number
# Factorial, in mathematics, the product of all positive integers
# less than or equal to a given positive integer and denoted by
# that integer and an exclamation point. Thus,
# factorial seven is written 7!, meaning 1 × 2 × 3 × 4 × 5 × 6 × 7.
print('\nExercise four Factorial of a number\n')

# number = input('Enter a number : ')
number = 5
factorial = 1
for i in range(1,int(number) + 1):
    factorial *= i
print(factorial)

# Exercise five Function to measure the distance between two points on graph

def distance(x1,y1,x2,y2):
    dist = pow(pow(x1 - x2, 2) + pow(y1 - y2, 2),0.5)
    return dist


print(str(distance(1,2,2,4)))