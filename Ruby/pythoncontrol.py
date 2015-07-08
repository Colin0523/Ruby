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