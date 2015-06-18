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



def pig(l):
    #l = raw_input("Please input a word: ")
    if l != type(str):
        print "Please input a word!"
    elif l.len() == 1: 
        print "Please input a word with more letters!"
    else:
        l = len(len(d) - len(d-1))
        print d + 'ay'
pig("a")











