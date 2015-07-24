count = 0

if count < 10:
    print "Hello, I am an if statement and count is", count
    
while count < 10:
    print "Hello, I am a while and count is", count
    count += 1

num = 1

while num <= 10:  # Fill in the condition
    print num **2# Print num squared
    num +=1# Increment num (make sure to do this!)

#choice = raw_input('Enjoying the course? (y/n)')

#while choice != "y" and choice != "n":  # Fill in the condition (before the colon)
#    choice = raw_input("Sorry, I didn't catch that. Enter again: ")

count = 0

while count < 10: # Add a colon
    print count
    count +=  1 # Increment count


import random

print "Lucky Numbers! 3 numbers will be generated."
print "If one of them is a '5', you lose!"

count = 0
while count < 3:
    num = random.randint(1, 6)
    print num
    if num == 5:
        print "Sorry, you lose!"
        break
    count += 1
else:
    print "You win!"




"""
from random import randint


# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3
# Start your game!
while guesses_left > 0:
    guess = int(raw_input("Your guess:"))
    if guess == random_number:
        print "You win!"
        break
    guesses_left -= 1 
else: 
    print "You lose."

"""


phrase = "A bird in the hand..."

# Add your for loop

for char in phrase:
    if char == "A" or char == "a":
        print "X",
    else:
        print char,


#Don't delete this print statement!
print


numbers  = [7, 9, 12, 54, 99]

print "This list contains: "

for num in numbers:
    print num

# Add your loop below!
for sq in numbers:
    print sq ** 2


d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}

for key in d:
    # Your code here!
    print key,d[key]

list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
    if a > b:
        print a,
    else:
        print b
    



























