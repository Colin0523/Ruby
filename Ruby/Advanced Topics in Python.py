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
