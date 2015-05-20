
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

 

		
		
