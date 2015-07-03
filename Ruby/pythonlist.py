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



