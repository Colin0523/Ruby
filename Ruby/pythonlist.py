# -*-coding:utf-8-*-

zoo_animals = ["pangolin", "cassowary", "sloth", "dog"];
# One animal is missing!

if len(zoo_animals) > 3:
	print "The first animal at the zoo is the " + zoo_animals[0]
	print "The second animal at the zoo is the " + zoo_animals[1]
	print "The third animal at the zoo is the " + zoo_animals[2]
	print "The fourth animal at the zoo is the " + zoo_animals[3]



##从0计数
numbers = [5, 6, 7, 8]

print "Adding the numbers at indices 0 and 2..."
print numbers[0] + numbers[2]
print "Adding the numbers at indices 1 and 3..."
# Your code here!
print numbers[1] + numbers[3]

#替换
zoo_animals = ["pangolin", "cassowary", "sloth", "tiger"]
# Last night our zoo's sloth brutally attacked 
#the poor tiger and ate it whole.

# The ferocious sloth has been replaced by a friendly hyena.
zoo_animals[2] = "hyena"

# What shall fill the void left by our dear departed tiger?
# Your code here!
zoo_animals[3] = "panda"




##append
suitcase = [] 
suitcase.append("sunglasses")

# Your code here!
suitcase.append("clothes")
suitcase.append("pants")
suitcase.append("hats")



list_length = len(suitcase) # Set this to the length of suitcase

print "There are %d items in the suitcase." % (list_length)
print suitcase



##slice
suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]

first  = suitcase[0:2]  # The first and second items (index zero and one)
middle = suitcase[2:4]               # Third and fourth items (index two and three)
last   = suitcase[4:6]                # The last two items (index four and five)



##slice list strings
animals = "catdogfrog"
cat  = animals[:3]   # The first three characters of animals
dog  = animals[3:6]              # The fourth through sixth characters
frog = animals[6:]      # From the seventh character to the end



##index and insert
animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck")    # Use index() to find "duck"

# Your code here!
print animals.insert(duck_index,"cobra")


print animals # Observe what prints after the insert operation



##for loop
my_list = [1,9,3,8,5,7]

for number in my_list:
    print number *2



##sort 
start_list = [5, 3, 1, 2, 4]
square_list = []

# Your code here!
for square in start_list:
    x = square ** 2
    square_list.append(x)
    square_list.sort()

print square_list


#字典
# Assigning a dictionary with three key-value pairs to residents:
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}

print residents['Puffin'] # Prints Puffin's room number

# Your code here!
print residents['Sloth'] 
print residents['Burmese Python'] 


#add elements to dictionary
menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print menu['Chicken Alfredo']

# Your code here: Add some dish-price pairs to menu!
menu['Beef'] = 12
menu['Noodles'] = 8
menu['Rice'] = 2




print "There are " + str(len(menu)) + " items on the menu."
print menu


#字典添加删除元素
# key - animal_name : value - location 
zoo_animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',
'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'}
# A dictionary (or list) declaration may break across multiple lines

# Removing the 'Unicorn' entry. (Unicorns are incredibly expensive.)
del zoo_animals['Unicorn']

# Your code here!
del zoo_animals['Sloth']
del zoo_animals['Bengal Tiger']
zoo_animals['Rockhopper Penguin'] = 'Exhibit'

print zoo_animals


#添加删除元素
inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
  
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 

# Your code here
inventory['pocket'] =  ['seashell','strange berry','lint']
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold'] = 550

########################list tips
#n.pop(index) will remove the item at index from the list and return it to you:n = [1, 3, 5]
#n.pop(1)
# Returns 3 (the item at index 1)
#print n
# prints [1, 5]

#n.remove(item) will remove the actual item if it finds it:
#n.remove(1)
# Removes 1 from the list,
# NOT the item at index 1
#print n
# prints [3, 5]
#del(n[1]) is like .pop in that it will remove the item at the given index, but it won't return it:
#del(n[1])
# Doesn't return anything
#print n
# prints [1, 5]
###########################


n = [3, 5, 7]
def double_list(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x
# Don't forget to return your new list!

print double_list(n)



def my_function(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x

print my_function(range(3)) # Add your range between the parentheses!



n = [3, 5, 7]
def total(numbers):
    result = 0
    for i in range(len(numbers)):
        result += numbers[i] 
    return result
    
total(n)




n = ["Michael", "Lieberman"]
# Add your function here
def join_strings(words):
    result = ""
    for w in range(len(words)):
        result += words[w]
    return result
    

print join_strings(n)




m = [1, 2, 3]
n = [4, 5, 6]

# Add your code here!
def join_lists(x,y):
    return x + y 


print join_lists(m, n)
# You want this to print [1, 2, 3, 4, 5, 6]

n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here
def flatten(lists):
    result = []
    for numbers in lists:
        for item in numbers:
            result.append(item)
    return result
print flatten(n)






