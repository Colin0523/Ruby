# -*-coding: utf-8 -*-
#for
webster = {
	"Aardvark" : "A star of a popular children's cartoon show.",
    "Baa" : "The sound a goat makes.",
    "Carpet": "Goes on the floor.",
    "Dab": "A small amount."
}

# Add your code below!
for key in webster:
    print webster[key]


a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
for num in a:
    if num % 2 == 0:
        print num


#list functions
def fizz_count(x):
    count = 0
    for item in x:
        if item == 'fizz':
            count += 1
        
    
    print '次数是'+  str(count)
  
fizz = ["fizz","cat","fizz"]
fizz_count(fizz)


#example
prices = {
    "banana" : 4, "apple" : 2,
    "orange" : 1.5,"pear" : 3 
}

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
total = 0
for key in prices:
    print key
    print "price: %s"%prices[key]
    print "stock: %s" %stock[key]
    total += prices[key] * stock[key]
    print "toatl:" + str(total)

#shopping list
shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
    
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Write your code below!
def compute_bill(food):
    total = 0
    for key in food:
        print "food: %s"%key,
        print "prices: %s " %prices[key]
        total += prices[key]
    return total
    print total

compute_bill(shopping_list)

#panduan
shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
    
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Write your code below!
def compute_bill(food):
    total = 0
    for key in food:
       if stock[key] > 0:
            total += prices[key]
            stock[key] = stock[key] - 1
       else:
            print "Out of %s" % key
    return total
  
#lesson number one
lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

students = [lloyd, alice, tyler]


