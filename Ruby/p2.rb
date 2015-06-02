#注释
#This entire line  is  a comment
#x = "#{}This is  a string"
y = /#This is a regular expression/

#p x
p y

=begin
 Any code here is commented out
=end

#if循环
x = 1
while x < 10 do
    print x
    x = x + 1
end



3.times {print "ruby "}


1.upto(10) do |x|
    print x
end


#块结构
module Stats
	class Dateset
		def initialize(filename)
			IO.foreach(filename) do |line| #A block in the method
				if line [0,1] == "#"      #An if statement in the block
                    next
                end
                
			end
		end
	end	
end	

#文件结构
#!/usr/bin/ruby -W shebang comment
# _*_ coding: utf-8 _*_ coding comment
#require 'socket'    load networking library

#...               program goes here

#_END_             mark end of  code

#...               program date  goes here



#3.2.4访问字符和字符串
p s = 'hello'
p	s[0]            #first character 
p 	s[s.length-1]   #last character
p 	s[-1]           #last character
p 	s[-2]           #the second-to-last character
p 	s[-s.length]    #the second-to-last character
p 	s[s.length]     #no character return nil 



#数组
p words = %w[this is a test]
p open = %w|( [ { < } |
p white = %w(\s \t \r \n)


p array = Array.new(10) {|i| i+1 }

p a = [0,1,4,9,16]
p a[0] = "zero"
p a

b = ('a'..'e').to_a
p b[0,0]
p b[1,1]
p b[-2,2]
p b[0,2] 
p b[-2..-1] 
p b[0..-1]


p b[0,2] = %w[A B]
b[2..5] = %w[C D E]
b[0..1] = []
p b

p a + b 
p b + [1,1,1,1,1]

p b << 2 << 3
p b << [2,3,4]
p b[0..1] = [] 
p b 

#哈希
numbers = Hash.new 
numbers["one"] = 1 
numbers["two"] = 2 
numbers["three"] =3
sum = numbers["one"] + numbers["two"]
p sum

num = {:one => 1,:two => 2, :three => 3}

#范围
r = 'a'..'c'
r.each {|l| print'r' "[#{l}]"}
r.step(2) {|l| p "[#{l}]"}
p r.to_a

p  (1..3).to_a


#3.5.1测试一个range的成员关系
r = 0...100 
p r.member? 50
p r.include? 100
p r.include? 99.9


p "cover?"
triples = "AAA"..."ZZZ"
p triples.include? "ABC" 
p triples.include? "ABCD"
#p triples.cover? "ABCD"
p triples.to_a.include? "ABCD"


#3.6符号
:symbol
:"symbol"
:'another long symbol'
s = 'string'
sym = :"#{s}"

=begin
	
name = :size
if o.respond_to? name
	o.send(name)
end

str = "string" #Begin with a string 
sym = str.intern #convert to a symbol
sym = str.to_sym #Another way to do the same thing 
str = sym.to_s #Covert back to a string
str = sym.id2nmae #Another way to do it


=end





#3.7  true, false ,nil
o =nil
p o.nil?

#3.8 对象
s =  "Ruby" #Create a String object.Store a reference to it in s 
t = s       #Copy the reference to t.s and t both refer to the same object
t[-1] = ""  #Modify the object through the reference in t 
print s     #Access the modified object through s. print "Rub"
t = "Java"  #t now refer to a different object
print s,t   #Prints "RubJava"

#3.8.4 对象的类和对象的类型
p o.class == String      #true if is o a String
p o.instance_of? String  #true if is o a String


x = 1                      #This is the value we're working with
x.instance_of? Fixnum      #true: is an instance of Fixum
x.instance_of? Numeric     #false: instance_of? doesn't check inheritance
#x.is_a? Fixum              #true: is a Fixnum
x.is_a? Integer            #true: is an integer
x.is_a? Numeric            #true: is a Numeric
x.is_a? Comparable		   #true: works with mixin modules ,too
#x.is_a? object			   #true for any valuse of x 
Numeric === x       	   #true: x is_a Numeric

#3.8.5对象的相等性
a = "Ruby"		#One reference to one String object
b = c = "Ruby"	#Two references to another String object
p a.equal?(b) 	#false: a and b are different objects
p b.equal?(c)	#ture: b and c are refer to the same object

p a.object_id == b.object_id #words like a.equal?(b)

a = "Ruby"
b = "Ruby"
p a.equal?(b) #false: a and b do not refer to the same object
p a == b      #true： but these two distinct objects have euqal values

#3.8.5 ===操作符
(1..10) === 5     #true: 5 is in the range 1..10
/\d+/ === "123"	  #true: the string matches the regular expression
String === "s"    #true: "s" is an instance of the class String
p :s === "s"		  #true in Ruby 1.9.2


#4.4方法调用
puts "hello world" #puts invoked on self,with one string tag
Math.sqrt(2)       #sqrt invoked on object Math with an arg
#message.length     #length invoked on object message :no args 
#a.each {|x| p x}   #each invoked on object a,with an associated block

#4.5赋值
x = 1 
x += 1
x,y,z = 1,2,3

class Ambiguous
	def x; 1; end  #A method named x.Always returns 1

	def test 
		puts x		#No variable has been seen;refers to method above:prints 1
		
		#The lince below is never evaluated,because of the "if false"clause.But
		#the parser sees it and treats x as a variable for the reset of the method 
		x = 0 if false

		puts x  #x is a variable,but has never been assigend to: prints nil 

		x = 2 	#This is assignment does get evaluated
		puts x	#So now this line prints 2
    end
end

#4.6.14


#7.1.4 定义to_s 方法
=begin
	
class Point
	def initialize(x,y)
		@x,@y = x,y
	end

	def to_s            #Return a String that represents this point 
		"(#@x,#@y)"     #Just interpolate the instance variables into a string
	end
end

p = new Point(10,20)   #Create a new Point object 
puts p 				   #Display "(1,2)"

=end

#类，对象
class  Person
	def initialize(name,age = 18)
		@name = name
		@age =  age 
		@motherland = "China"
	end

	def  talk
		puts "My name is #{@name}, age is #{@age}, motherland is #{@motherland}"

	 	
	end
end

p = Person.new('csl') 
p.talk


#例子
class Customer 
	@@no_of_customer = 0
	def initialize(id,name,addr)
		@cust_id = id 
		@cust_name = name 
		@cust_addr = addr 
	end
    #打印客户信息
	def dispaly_details()
		puts "Customer id  #{@cust_id}"
		puts "Customer name  is #{@cust_name}"
		puts "Customer address is #{@cust_addr}"
	end
	#统计客户数量
	def total_no_of_customers()
		@@no_of_customer += 1
		puts "Total number of customers: #{@@no_of_customer} "
	end
end

#创建两个客户：
cust1 = Customer.new("1","John","Wisdom Apartments")
cust2 = Customer.new("2","Poul","New Empire")


#调用方法
cust1.dispaly_details()
cust1.total_no_of_customers()

cust2.dispaly_details()
cust2.total_no_of_customers()


#全局变量
$global_variable = 10 
class Class1
	def print_gloable1

		puts "Gloable variable in Class1 is #{$global_variable}"
		
	end
end

class Class2 
	def print_gloable2

		puts "Gloable variable in Class2 is #{$global_variable}"
		
	end
end 

#生成对象
class1obj1 = Class1.new
class1obj2 = Class2.new

class1obj1.print_gloable1
class1obj2.print_gloable2 
 


#实例变量
class Customer 
	def initialize(id,name,addr)
 
 		@cust_id = id 
 		@cust_name = name 
 		@cust_addr = addr 
 	end

 	def display_details()

 		puts "Customer id #{@cust_id}"
 		puts "Customer name #{@cust_name}"
 		puts "Customer addr #{@cust_addr}"
 	end
end 


#创建对象
cust1 = Customer.new("1","Max","Apartments")
cust2 = Customer.new("2","Jack","Khadala")

#调用方法
cust1.display_details()
cust2.display_details()


#常量
class Example
	VAR1 = 100
	VAR2 = 50

	def show 
		puts "Value of first Constant is #{VAR1}"
		puts "Value of second Constant is #{VAR2}"
	end
end 

object = Example.new 
object.show



#Ruby 点运算符. 和双冒号运算符::
MR_COUNT = 0 #定义在object 类上的常量
module FOO
	MR_COUNT = 0 
#	::MR_COUNT =1 #设置全局变量为1
#	MR_COUNT =2 #设置局部计数为2
end 

puts MR_COUNT #全局常量
puts FOO::MR_COUNT #FOO的局部常量

#第二个实例
CONST = "out there"
class Inside_one
	CONST = proc {'in there'}
	def where_is_my_const
		::CONST + "inside_one"
	end
end

class Inside_two
	CONST = 'inside_two'
	def where_is_my_const
		CONST
	end
end


puts Inside_one.new.where_is_my_const
puts Inside_two.new.where_is_my_const
puts Object::CONST + Inside_two::CONST
puts Inside_two::CONST + CONST
puts Inside_one::CONST
puts Inside_one::CONST.call + Inside_two::CONST

#判断
x = 1
if x > 2
	puts "X is greater than 2"
elsif x <=2 and x != 0
	puts "X is 1"
else 
	puts "I can't guess the number"
end 

#if修饰符
$debug = 1
print "debug\n" if $debug

#unless

x = 1
unless x > 2
	puts "X is less than 2"

else 
	puts "x  is greater than 2"
	
end

#unless修饰符
$var = 1
print "1 -- Value is set\n " if $var
print "2 --Value is set\n " unless $var

$var = false
print = "3 -- Value is set\n" unless $var
	
#case语句
$age = 24
case $age 
when 0 .. 2
	puts 'baby'
when 3 .. 6
	puts 'little child'
when 7 .. 12
	puts 'child'
when 13 .. 18
	puts 'youth'
else
	puts 'adult'
end
	
		
#while循环
$i = 0
$num = 5

while $i < $num do
	puts ("Inside the loop i = #{$i}")
	$i += 1	
end

#while修饰符
$p = 0
$sum = 5
begin
	puts ("Inside loop p = #{$p}")
	$p += 1
end while $p < $num

#until语句
$u = 0
until $u > $num do 
	puts "Inside loop u= #{$u}"
	$u += 1;
end

#for循环
for i in 0 .. 5
	puts "Value of local variable is #{i}"
end 

(0 .. 5).each do |o|
	puts "The Value of local variable is #{o}"
end

for i in 0 .. 5
	if i > 2 then 
		break
	end 
	puts "i is #{i}"
end 

for b in 0 .. 5
	if b < 2 then 
		next
	end 
	puts "issss is #{b}"
end 

#方法
def test(a1 = "Ruby",a2 = "Perl")
	puts "The programming language is #{a1}"
	puts "The programming language is #{a2}"
end 

test "C","C++"
test

#返回值
def test
	i = 100
	j = 200
	k = 300
    return i,j,k
end
var = test
puts var

#可变数量的参数
def sample(*test)
	puts "The number of parameters is #{test.length}"
	for  i in 0 .. test.length
		puts "The number of parameters are #{test[i]}"
	end
end
sample "Zara","6","F"
sample "Mac","36","M","MCA"

#类方法

#alias语句
#alias method method
#alias $global_variable $global_variable

#yield语句
def test
	puts "You are in the method"
	yield 5
	puts "You are again back to the method"
	yield
end 
test {puts "You are in the block"}
	
def  test
	yield 7
	puts "You are in the method test"
	yield 100
	
end
test {|a| puts "You are in the block #{a}"}


#块和方法
def test(&block)
	block.call
	
end
test {puts "Hello World"}

#模块
module Trig
	PI = 3.141592654
	def Trig.sin(x)

	# .. 
	end 

	def Trig.cos(x)
	#..
	end
end 

y = Trig.cos(Trig::PI/4)

module Week
   FIRST_DAY = "Sunday"
   def Week.weeks_in_month
      puts "You have four weeks in a month"
   end
   def Week.weeks_in_year
      puts "You have 52 weeks in a year"
   end
end


class Decade
include Week
   no_of_yrs=10
   def no_of_months
      puts Week::FIRST_DAY
      number=10*12
      puts number
   end
end
d1=Decade.new
puts Week::FIRST_DAY
Week.weeks_in_month
Week.weeks_in_year
d1.no_of_months

#Mixin
module A
   def a1
   end
   def a2
   end
end
module B
   def b1
   end
   def b2
   end
end

class Sample
include A
include B
   def s1
   end
end

samp=Sample.new
samp.a1
samp.a2
samp.b1
samp.b2
samp.s1

#表达式置换
x, y, z  = 12, 36, 72
puts "The value of x is #{x}."
puts "The sum of x and y is  #{x + y}."
puts "The average of was  #{(x + y + z)/3}."

#字符串内建方法
myStr = String.new(str = "THIS IS TEST")
foo = myStr.downcase
puts "#{foo}"


#数组
names = Array.new(20) 
puts names.size
puts names.length
#names (4,'mac')
puts names 

#范围Range
#.作为序列的范围
#.作为条件的范围
#.作为间隔的范围

#作为序列的范围
range1 = (1 .. 10).to_a
range2 = ('bar' .. 'bat').to_a
puts "#{range1}"
puts "#{range2}"

#Assume a range 
digits = 0 .. 9
puts digits.include?(5)
ret = digits.min
puts "Min value is #{ret}"

ret = digits.max
puts "Max values is #{ret}"

ret = digits.reject{|i| i < 5}
puts "Rejected values are #{ret}"

digits.each do |digit|
	puts "In Loop #{digit}"
end

#作为条件的范围
score  = 90
result = case score	
	when 0 .. 40: "Fail"
	when 41 .. 60: "Pass"
	when 61 .. 70: "Pass with Merit"
	when 71 .. 100: "Pass with Distinction"
	else "Invalid Score"
end
puts result

#作为间隔的范围
if ((1 .. 10) === 5)
	puts "5 lies in (1 .. 10)"
end

if (('a' .. 'j') === 'c')
	puts "c lies in ('a' .. 'j')"
end

if (('a' .. 'j') === 'z')
	puts "z lies in ('a' .. 'j')"
else 
	puts "z lies is not in ('a' .. 'j')"
end

#Ruby迭代器
#迭代器是集合支持的方法。存储一组数据成员的对象称
#为集合,在 Ruby 中，数组和散列可以称之为集合
#each迭代器

ary = [1,2,3,4,5]
ary.each do |i|
	puts i
end

#collect迭代器
#collect 方法不需要总是与一个块关联
#collect 方法返回整个集合，不管它是数组或者是哈希。
a = [1,2,3,4,5]
b = Array.new
b = a.collect
puts b 

a = [1,2,3,4,5]
b = a.collect {|x| 10*x}
puts b


























