
a = [1,2,3,4]
b = a.map { |x| x*x  }
c = a.select { |x| x%2 == 0}
a.inject do |sum,x|
	sum + x
end
print a
print b
print c


h = {
	:one => 1,
	:two => 2
}
h[:one]
h[:three] =3 
h.each do |key,value|
	print "#{value}:#{key}};"
end


p 'ddd1'+'ddd2'
p 'Ruby ' * 3

max = 5 > 3 ? 3 : 5
print max 

def Math.ss(x)
	x = x * x
	print x
end
p Math.ss(10)



def are_you_sure?    #define a method. Note question mark!
	while true       #Loop until we explicitly return
		print "Are you sure? [y/n]:"  #Ask the user a question 
		reponse = gets    #Get answer
		case response     #Begin case conditional 
		when /^[yY]/      #If reponse begins with y or Y
			return true   #Return true from the method
			
		when /^[nN]/,/^$/      #If reponse begins with n,N or is empty
			return false    #Rrturn false
		end
	end
end

			
9.downto(1) {|n| print n }	
puts "blastoff!"	

 
#数组
names = Array.new(4,"mac") 
puts "#{names}"
		
nums = Array.new(10) {|e| e = e *2 }
puts "#{nums}"	

digits = Array(0 .. 9)
puts "#{digits}"

digits = Array(0 ..9)
num = digits.at(6)
puts num

#压缩数据
a = ["a","b","c"]
n = [65,66,67]
puts a.pack("A3A3A3")
puts a.pack("a3a3a3")
puts n.pack("ccc")

#哈希
months = Hash.new {"month"}
puts "#{months[0]}"
puts "#{months[72]}"

H = Hash["a" => 100,"b" => 200]
puts "#{H['a']}"
puts "#{H['b']}"

#哈希内建方法
$, = ", "
months = Hash.new("month")
months = {"1" => "January", "2" => "Feburary"}
keys = months.keys
puts "#{keys}"

#日期，时间
time1 = Time.new
puts "Current Time: "+ time1.inspect

#Time.now 是一个同义词
time2  = Time.now
puts "Current time: " + time2.inspect


	
=begin

#获取Date&Time组件
time = Time.new
puts "Current Time: " + time.inspect
puts time.year
puts time.month
puts time.day
puts time.wday #一周中的星期几
puts time.yday #一年中的第几天
puts time.hour #23:24小时制　　　
puts time.min  #59
#puts time.sec　#59 　　　　
#puts time.usec　　#微秒 999999
puts time.zone   #时区

=end


time = Time.new
values = time.to_a
p Time.utc(*values)

#返回从纪元以来的秒数
time = Time.now.to_i
p time

#把秒数转换为Time对象
time1 = Time.at(time)
p time1

#返回从纪元以来的秒数，包含微秒
time3 = Time.now.to_f
p time3

#时间算法
now = Time.now  #当前时间
puts now

past = now - 10 #10秒之前
puts past

future = now + 10 #从现在开始10秒之后
puts future

diff = future - now
puts diff

