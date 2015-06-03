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

end 

#创建对象
box = Box.new(10,20)
x = box.PrintWidth()
y = box.PrintHeight()
puts "width of box is: #{x}"
puts "height of box is: #{y}"

