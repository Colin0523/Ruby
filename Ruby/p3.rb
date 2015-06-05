#面向对象
#initialize 方法
#实例变量
# class Box
# 	def initialize(w,h)
# 		#给实例变量赋值
# 		@width,@height = w,h 
		
# 	end
# end 

#访问器&设置器 方法
class Box
	#构造器方法
	def initialize(w,h)
		@width,@height = w,h
	end
	#访问器方法
	def PrintWidth
		@width
	end

	def PrintHeight
		@height
	end	

	#设置器方法
	def setWidth(value)
		@width1 = value
	end

	def setHeight(value)
		@height1 = value 
	end

	#访问器方法
	def getWidth
		@width1
		
	end

	def getHeight
		@height1
	end 
end 

#创建对象
box = Box.new(10,20)
x = box.PrintWidth()
y = box.PrintHeight()
puts "width of box is: #{x}"
puts "height of box is: #{y}"

#使用设置器方法
box.setWidth(30)
box.setHeight(50)

#使用访问器方法
x = box.getWidth()
y = box.getHeight()

puts "Width of the box is : #{x}"
puts "Width of the box is : #{y}"

#实例方法
class BoxOne
	#constructor method
	def initialize(wid,hei)
        @width_one = wid
        @height_one = hei		
	end

	#实例方法
	def getArea
		@width_one * @height_one
	end 
end 

#创建对象
boxt = BoxOne.new(100,200)

#调用实例方法
s  = boxt.getArea()
puts "Area of the box is: #{s}"

#类方法&类变量
class BoxTwo
	#初始化类变量
	@@count = 0 
	def initialize(w,h)
		#给实例变量赋值
		@width  = w 
		@height = h 
		@@count += 1

	end

	def sum
		puts @width + @height
	end

	def self.printCount()
		puts "Box count is: #{@@count}"
		
	end
end 

#创建两个对象
box1 = BoxTwo.new(25,50)
box2 = BoxTwo.new(35,70)

#调用类方法来输出盒子计数
BoxTwo.printCount()

#to_s方法
class BoxThree
	#构造器方法
	def initialize(w,h)
		@width = w
		@height = h
	end 

	#定义to_s方法
	def to_s
		"(w:#{@width}, h:#{@height})"
	end 
end 

#创建对象
box3 = BoxThree.new(55,110)

#自动调用to_S方法
puts "String representation of box is #{box3}"


#访问控制
class BoxFour
	#构造器方法
	def initialize(w,h)
		@width, @height = w,h
	end 

	#实例方法默认是public的
	def getArea
		getWidth() * getHeight
	end 

	#定义private的访问器法
	def getWidth
		@width
	end 

	def getHeight
		@height
	end

	#make them private
	private :getWidth, :getHeight

	#用于输出面积的实例方法
	def printArea
		@area = getWidth() * getHeight
		puts "Big box area is : #{@area}"
	end 

	#让实例方法是protected的
	protected :printArea
end 

#创建对象
box4 = BoxFour.new(99,101)

#调用实例方法
a = box4.getArea()
puts "Area of the box is :#{a}"

#尝试调用protected的实例方法
#box4.printArea

#类的继承
class BoxFive
	#构造器方法
	def initialize(w,h)
		@width,@height = w,h

	end

	#实例方法
	def getAera
		@width * @height
		
	end

end 

#定义子类
class BigBox < BoxFive
	#添加一个新的实例方法
	def printArea
		@area = @width * @height
		puts "Big box area is : #{@area}"
	end
end 

#创建对象
box5 = BigBox.new(55,45)

#输出面积
box5.printArea()

#方法重载
class BoxSix
	#构造器方法
	def initialize(w,h)
		@width,@height = w, h
	end 

	#实例方法
	def getArea
		@width * @height
	end 
end 

#定义子类
class BigBox2 < BoxSix
	#改变已有的getArea方法
	def getArea
		@area = @width ** @height
		puts "Big box area is : #{@area}"
	end 
end 

#创建对象
box6 = BigBox2.new(12,5)

#使用重载的方法输出结果
box6.getArea

#运算符重载
class BoxSeven
	#构造器方法
	def initialize(w,h) #初始化width和height
		@width,@height = w, h
	end 

	#定义 + 来执行向量加法
	def +(other)
		BoxSeven.new(@width + other.width, @height + other.height )
	end 

	#定义一元运算符 - 来对width和height求反
	def -@
		BoxSeven.new(-@width,-@height)
	end 
 
 	#执行向量乘法
 	def *(scalar)
 		Box.new(@width*scalar, @height*scalar)
 	end
end 

#冻结对象
class BoxEight
	def initialize(w,h) #初始化width和height
		@width,@height = w, h
	end 

	#访问器方法
	def getWidth
		@width
	end 

	def getHeight
		@height
	end

	#设置器方法
	def setWidth8(value)
		@width = value
	end 

	def setHeight8(value)
		@height = value
	end 
end 

#创建对象
box8 = BoxEight.new(6,23)

#冻结对象
# box8.freeze
# if(box8.frozen?)
# 	puts "Box object is frozen object"
# else
# 	puts "Box object is normal object"
# end 

# #尝试使用设置器方法
# box8.setWidth8(6)
# box8.setHeight8(23)

# #使用访问器方法
# x8 = box8.getWidth
# y8 = box.getHeight

# puts "Width of the box is: #{x8}"
# puts "Width of the box is: #{y8}"



#类常量
class BoxNine
	BOX_COMPANY = "TATA Inc"
	BOXWEIGHT = 10

	def initialize(w,h)
		@width, @height = w, h 
		
	end

 	#实例方法
 	def getArea
 		@width * @height
 	end 
end

#创建对象
box9 = BoxNine.new(23,25)

#调用实例方法
a = box9.getArea()
puts "Area of the box is: #{a}"
puts BoxNine::BOX_COMPANY
puts "Box weight is: #{BoxNine::BOXWEIGHT}"


#使用allocate


























