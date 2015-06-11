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
		print ("Total Employee %d " % Employee.empCount)

	def displayEmployee(self):
		print ("Name : " ,self.name, ",Salary: " ,self.salary)


"创建Employee 类的第一个对象"
emp1 = Employee("Zara", 2000)

"创建Employee 类的第一个对象"
emp2 = Employee("Manni",5000)

emp1.displayEmployee()
emp2.displayEmployee()

print ("Total Employee %d " % Employee.empCount)

#python函数
def printme(str):
	"打印任何传入的字符串"
	print (str);
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































