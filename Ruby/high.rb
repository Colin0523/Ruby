#正则表达式

line1 = "Cats are smarter than dogs"
line2 = "Dogs also like meat"

if (line1 =~ /Cat(.*)/)
	puts "Line1 contains Cats"
end


if (line2 =~ /Cat(.*)/)
	puts "Line2 contains Dogs"
end 


#搜索和替换
phone = "2004-959-559 #This is phone number"

#删除Ruby的注释
phone = phone.sub!(/#.*$/, "")
puts "phone Num: #{phone}"

#移除除数字之外的其他字符
phone = phone.gsub!(/\D/,"")
puts "phone number: #{phone}"


text = "rails are rails, really good Ruby on Rails"
#把所有的rails改为Rails
text.gsub!("rails","Rails")
puts "Text1 : #{text}"

#把所有的单词Rails都改成首字母大写
text.gsub!(/\brails\b/,"Rails")
puts "Text2 : #{text}"

