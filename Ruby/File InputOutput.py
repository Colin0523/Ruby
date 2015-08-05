my_list = [i**2 for i in range(1,11)]
# Generates a list of squares of the numbers 1 - 10

f = open("output.txt", "w")

for item in my_list:
    f.write(str(item) + "\n")

f.close()

my_file = open("output.txt","r+")



my_list = [i**2 for i in range(1,11)]
my_file = open("output.txt", "r+")

# Add your code below!
for item in my_list:
    my_file.write(str(item) + "\n")
my_file.close()


my_file = open("output.txt", "r")
print my_file.read()
my_file.close()

my_file = open("text.txt","r")
print my_file.readline()
print my_file.readline()
print my_file.readline()
my_file.close()


with  open("text.txt","r+") as tex1:
    tex1.write("test")

if my_file.closed is not True:
    tex1.close()