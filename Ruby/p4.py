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

