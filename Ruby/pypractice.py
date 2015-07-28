def digit_sum(n):
	c = str(n)
	total = 0
	for i in c:
		 
		
		total += int(i) 
	print total
		
			  
n = 123456
digit_sum(n)

def factorial(x):
	total =1
   	if x == 0:
   		print 1
   	else:
   		o = 1
   		while o <= x:
   			total *= o 
   			o += 1
   		print total
      

print factorial(4)

'''
def is_prime(x):
  if x <= 1:
    return False

  i = 2
  while i * i <= x:
    if x % i == 0:
    	print 'False'
    	i += 1 
  print 'True'
'''


def reverse(text):
  text1 = ""
  for i in range(len(text)):
    text1 += text[-1-i]
  return text1 


vowels = "aeiouAEIOU"
def anti_vowel(text):
    new_word = ""
    for char in text:
        if char in vowels:
            new_word += ""
        else:
            new_word += char
    return new_word

print anti_vowel("Hey You!")




score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}


def scrabble_score(word):
  total = 0
  lower = str.lower(word)
  print lower
  for i in lower:
    sc = score[i]
    total += sc
  print total
scrabble_score('ACB')


def censor(text,word):
  string = text.split(" ")
  newtext = []
  for i in string:
    print i,
    if i == word:
      i = '*' * len(word)
      newtext.append(i)
    else:
      newtext.append(i) 
  print " ".join(newtext) 
    
        
censor ("ty to do exercise",'exercise')

n = 'dad'
a = " ".join(n) 
print  a


def count(sequence,item):
    count = 0 
    for co in sequence:
        if item == co:
            count +=1
    print count

def purify(l):
    n = []
    for a in l:
        if a % 2 == 0:
            n.append(a)
    print n

c = [1,2,3,4,5]
purify(c)

def product(l):
    total = 1
    for num in l:
       total *= num
       print total
    return total 


def remove_duplicates(l):
    n = []
    for ele in l:
        if ele not in n:
            n.append(ele)
    return n 
        

l = [6, 8, 12, 2, 23]
def median(l):
    total = sum(l)
    print total 
    length = len(l)
    print length
    middle = float(total)/length
    return middle

print median(l)

def median(ListIn):
    ListIn = sorted(ListIn)
    n = len(ListIn)
    if n % 2 == 0:
        return (ListIn[n/2-1] + ListIn[n/2])/2.0
    else:
        return ListIn[(n-1)/2]


