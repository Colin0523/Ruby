my_dict = { 
    "Name": "Colin",
    "Age": 20,
    "A": True
}
print my_dict.keys()
print my_dict.values()

for key in my_dict:
    print key,my_dict[key]

doubles_by_3 = [x*2 for x in range(1,6) if (x*2) % 3 == 0]

# Complete the following line. Use the line above for help.
even_squares = [x**2 for x in range(1,11) if x % 2 == 0]

print even_squares

cubes_by_four = [x ** 3 for x in range(1,11) if x ** 3 % 4 == 0]
print cubes_by_four

to_21 = [x for x in range(1,22)]

odds = to_21[::2]

middle_third = to_21[7:14]


my_list = range(16)
filter(lambda x: x % 3 == 0, my_list)

languages = ["HTML", "JavaScript", "Python", "Ruby"]
print filter(lambda x: x == "Python", languages)

threes_and_fives = [x for x in range(1,16) if x % 3 == 0 or x % 5 == 0]
print threes_and_fives

garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
message = garbled[-1::-2]
print message


garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message = filter(lambda x: x != 'X',garbled)
print message 