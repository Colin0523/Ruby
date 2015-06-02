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

#Ruby文件的输入与输出
#Ruby 提供了一整套 I/O 相关的方法，在内核（Kernel）
#模块中实现。所有的 I/O 方法派生自 IO 类。
#类 IO 提供了所有基础的方法，
#比如 read、 write、 gets、 puts、 readline、 getc 
#和 printf

#puts 语句
#puts 语句指示程序显示存储在变量中的值。
val1 = "This is valuable one"
val2 = "This is valuable Tow"
puts val1
puts val2

#gets 语句
#gets 语句可用于获取来自名为 
#STDIN 的标准屏幕的用户输入
puts "Enter a value: "
va3 = gets
puts va3

#putc 语句
#putc 语句可用于依次输出一个字符
str = "Hello Ruby"
putc str

#print语句
#puts 语句在输出内容后会跳到下一行，
#而使用 print 语句时，光标定位在同一行
print "Hello World\n"
print "Good Morning"

#打开和关闭文件
#File.new方法
#aFile = File.new("filename", "mode")
   # ... 处理文件
#aFile.close


#File.open 方法
#File.open("filename", "mode") do |aFile|
   # ... process the file
#end

#sysread方法
#输入文本文件：
#This is a simple text file for testing purpose.
#aFile = File.new("input.txt","r")
#if aFile
#	content = aFile.sysread(20)
#	puts content
#else 
#	puts "Unable to open file"
#end

#syswrite 方法
#当使用方法 syswrite 时，您需要以写入模式打开文件
#aFile = File.new("input.txt","r+")
#if aFile 
#	aFile.syswrite("ABCDEF")
#else
#	puts "Unable to open file!"
#end

#each_byte 方法
#each_byte 是个可以迭代字符串中每个字符
# aFile = File.new("input.txt", "r+")
# if aFile
#    aFile.syswrite("ABCDEF")
#    aFile.rewind
#    aFile.each_byte {|ch| putc ch; putc ?. }
# else
#    puts "Unable to open file!"
# end

#IO.readline方法
#该方法逐行返回文件的内容
# arr = IO.readlines("input.txt")
# puts arr[0]
# puts arr[1]

#IO.foreach 方法
#方法 foreach 不是返回一个数组
#IO.foreach("input.txt"){|block| puts block}

#重命名和删除文件
#重命名文件 test1.txt 为 test2.txt
#File.rename( "test1.txt", "test2.txt" )

#删除文件
#File.delete("asdasd.rb")

#文件模式与所有权
#使用带有掩码的 chmod 方法来改变文件的模式或权限/访问列表
# file = File.new( "test.txt", "w" )
# file.chmod( 0755 )

#文件查询
#检查文件是否存在
# a = File.open("file.rb") if File::exists?( "file.rb" )
# p "#{a}"
# #查询文件是否是文件
# a = File.file?("test.txt")
# p "#{a}"
# #查询是否是目录
# a = File::directory?( "/usr/local/bin" ) 
# p "#{a}"
# #文件
# a = File::directory?( "file.rb" )
# p "#{a}"
# #检查可读，可写，可执行 
# a = File.readable?( "test.txt" )   # => true
# p "#{a}"
# a = File.writable?( "test.txt" )   # => true
# p "#{a}"
# a = File.executable?( "test.txt" ) # => false
# p a
# #检查是否大小写为0
# a = File.zero?("test.txt")
# p a
# #返回文件大小
# #a = File.size("test.txt")
# p a 
# #检查文件类型
# a = File::ftype( "test.txt" )     # => file
# p a 

#目录
#改变当前目录
#Dir.chdir("/usr/bin")

#查看目录
puts Dir.pwd

#获取指定目录内的文件和目录列表
puts Dir.entries("E:/Ruby/Ruby").join(' ')

#Dir.foreach返回一个数组，包含指定目录内的所有项
Dir.foreach("E:/Ruby/Ruby") do |entry|
	puts entry
end

#获取目录列表的一个更简洁的方式是通过使用 Dir 的类数组的方法：
p Dir["E:/Ruby/Ruby/*"]

#创建目录
#Dir.mkdir("mynewdir2",755)

#删除目录
#Dir.delete("mynewdir2")

#创建临时目录
#Dir.tmpdir 提供了当前系统上临时目录的路径
#但是该方法默认情况下是不可用的
#为了让 Dir.tmpdir 可用，
#使用必需的 'tmpdir' 是必要的
require 'tmpdir'
   tempfilename = File.join(Dir.tmpdir, "tingtong")
   tempfile = File.new(tempfilename, "w")
   tempfile.puts "This is a temporary file"
   tempfile.close
   File.delete(tempfilename)

