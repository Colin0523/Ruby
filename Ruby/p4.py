#coding=utf-8

#python类
class Employee:
	'所有员工的基类'
	empCount = 0

	def __init__(self,name,salary):
		self.name = name
		self.salary = salary
		Employee.empCount += 1


	def displayCount(self):
		print "Total Employee %d " % Employee.empCount

	def displayEmployee(self):
		print "Name : " ,self.name, ",Salary: " ,self.salary


"创建Employee 类的第一个对象"
emp1 = Employee("Zara", 2000)

"创建Employee 类的第一个对象"
emp2 = Employee("Manni",5000)

emp1.displayEmployee()
emp2.displayEmployee()

print "Total Employee %d " % Employee.empCount

#python函数
def printme(str):
	"打印任何传入的字符串"
	print str;
	return;

#调用函数
printme("调用用户自定义函数")
printme("再次调用同一函数")

#可写函数说明
def changename(mylist):
	"修改传入的列表"
	mylist.append([1,2,3,4])
	print "函数内取值", mylist
	return
    

#调用changename函数
mylist = [10,20,30];
changename(mylist);
print "函数外取值：", mylist

#参数
def printinfo(name,age):
	print "Name :",name
	print "Age : ", age 
	return

#调用
printinfo("YX",17)

#不定长参数
def printinfot(arg1,*vartuple):
	"打印传入的任何参数"
	print "输出:"
	print arg1
	for var in vartuple:
		print var
	return;

#调用函数
printinfot(70,80,90)

#return
def sum(a1,a2):
	#返回两参数的和
	total = a1 + a2 
	print "Inside the function: ", total 
	return total;


#调用
sum(10,20)



#Date and Time 
from datetime import datetime
now = datetime.now()

print '%s/%s/%s %s:%s:%s' % (now.year,now.month,now.day,now.hour,now.minute,now.second)

#Conditionals & Control Flow
#And
bool_one =  False and False

bool_two =  -(-(-(-2))) == -2 and 4 >= 16**0.5

bool_three = 19 % 4 != 300 / 10 / 10 and False

bool_four = -(1**2) < 2**0 and 10 % 10 <= 20 - 10 * 2

bool_five = True and True



#And, Or, Not
# Use boolean expressions as appropriate on the lines below!

# Make me false!
bool_one = (2 <= 2) and "Alpha" == "Bravo"  # We did this one for you!

# Make me true!
bool_two = (1 == 2) or 2 == 2

# Make me false!
bool_three =  10 ** 10 == 50 and "A" == "a"

# Make me true!
bool_four =  not False and 1 == 1 
 
# Make me true!
bool_five =  1 < 10 and 50 > 25

#if 
def using_control_once():
    if 10/2.0 == 5:
        return "Success #1"

def using_control_again():
    if 100 > 10:
        return "Success #2"

print using_control_once()
print using_control_again()

#else
answer = "'Tis but a scratch!"

def black_knight():
    if answer == "'Tis but a scratch!":
        return True
    else:             
        return  False      # Make sure this returns False

def french_soldier():
    if answer == "Go away, or I shall taunt you a second time!":
        return True
    else:             
        return False       # Make sure this returns False

print black_knight()
print french_soldier()


#elif 
def greater_less_equal_5(answer):
    if answer > 5:
        return 1
    elif -1 < answer < 5:          
        return -1
    else:
        return 0
        
print greater_less_equal_5(4)
print greater_less_equal_5(5)
print greater_less_equal_5(6)



#translator game
#wrong way
# l = raw_input("Please input a word: ")
# if l != type("a"):

#         print "Please input a word!"

# elif l.len() == 1: 

#         print "Please input a word with more letters!"
# else:

#     l = len(len(l) - len(l-1))
#     print l + 'ay'



#right way 
# print 'Welcome to the Pig Latin Translator!'

# # Start coding here!
# pyg = 'ay'

# original = raw_input('Enter a word:')

# if len(original) > 0 and original.isalpha():
#     word = original.lower()
#     first = word[0]
    
#     new_word = word  + pyg
#     new_word [1:len(new_word)]
#     print new_word
   
# else:
#      print 'empty'


#function  方法内调用其他方法
def cube(number):
    mul = number ** 3
    return mul
    
def by_three(number):
    if number % 3 == 0:
        return cube(number)
        
    else:
        return False

#import
# Ask Python to print sqrt(25) on line 3.
import math
print math.sqrt(25)


#function import 引用指定模块的方法
from math import sqrt

#universal import 引用指定模块的所有方法
from math import *

#以下是指引用模块时注意方法名冲突
"""Universal imports may look great on the surface, but they're not a good idea for one very important reason: 

they fill your program with a ton of variable and function names without the safety of those names still being 

associated with the module(s) they came from.

If you have a function of your very own named sqrt and you import math, your function is safe: there is your sqrt a

nd there is math.sqrt. If you do from math import *, however, you have a problem: namely, two different functions with

 the exact same name.

Even if your own definitions don't directly conflict with names from imported modules, if you import * from several 

modules at once, you won't be able to figure out which variable or function came from where.

For these reasons, it's best to stick with either import module and type module.name or just import specific variables 

and functions from various modules as needed."""


#max,min,abs
maxmum = max(10,-100,3000)
print maxmum

minimum = min(10,-100,3000)
print minimum


absolute = abs(-80)
print absolute

#type
print type(41)
print type(80.5)
print type("hello")


#ex
def shut_down(s):
    if s == "yes":
        return "Shutting down"
    
    elif s == "no":
        return "Shutdown aborted"
    
    else:
        return "Sorry"


from math import sqrt
print sqrt(13689)

print type(False)


def distance_from_zero(thing):
    if type(thing)==int or type(thing)==float:
        return abs(thing)
        
    else:
        return "Nope"

#vacation cost
def hotel_cost(nights):
    return nights * 140


def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city =="Tampa":
        return 220
    elif city =="Pittsburgh":
        return 222
    elif city =="Los Angeles":
        return 475


def rental_car_cost(days):
    cost = days * 40
    if days <3:
        return cost
    elif days >= 3 and days < 7:
        return cost-20
    else:
        return  cost - 50

def trip_cost(city,days,spending_money):
    all_cost = hotel_cost(days) + rental_car_cost(days) + plane_ride_cost(city)+ spending_money
    print  "All_cost is: " + all_cost

trip_cost("Pittsburgh",10,100)
