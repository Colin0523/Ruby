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
p triples.cover? "ABCD"
p triples.to_a.include? "ABCD"


#3.6符号
:symbol
:"symbol"
:'another long symbol'
s = 'string'
sym = :"#{s}"

name = :size
if o.respond_to? name
	o.send(name)
end

str = "string" #Begin with a string 
sym = str.intern #convert to a symbol
sym = str.to_sym #Another way to do the same thing 
str = sym.to_s #Covert back to a string
str = sym.id2nmae #Another way to do it

#3.7  true, false ,nil

 

f  ff 








