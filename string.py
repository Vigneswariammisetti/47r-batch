# #counting the number of consonants in a string
# word="vigneswari"
# conso_count=0
# for i in range(len(word)):
#     c=word[i]
#     if c not in "aeiou":
#         conso_count+=1
# print(conso_count)

# #return chracters in the multiples of number
# def vowels(string,number):
#     for i in range(len(string)):
#         c=string[i]
#         if(i%number==0) and (c!=" "):
#          print(c,i)
# print(vowels("i am learning python",3))

# #using function count()
# def lower_upper_count(string):
#     upper_count=0
#     lower_count=0
#     for i in range(len(string)):
#         c=string[i]
#         if c==c.upper() and c!=" ":
#             upper_count+=1
#             print(upper_count)
#         elif c==c.lower() and c!=" ":
#             lower_count+=1
#             print(upper_count)
#             print(lower_count)
# print(lower_upper_count("Enjoy Every Moment"))

# username="panchabatla sarangapani"
# username="Panchabatla Sarangapani"
# print(username)

# #counting the no.of characters in a string
# name="lakshmi venkata padma naga lalitha"
# print(len(name))
# count=0
# for i in range(0,len(name)):
#     if name[i]!=" ":
#         count+=1
# print(count)

# #reversing a string
# word="nandan"
# last=len(word)-1
# for i in range(last,-1,-1):
#     print(word[i],end="")

# #counting the number of vowels in a string
# word="vigneswari"
# count=0
# for i in range(0,len(word)):
#     c=word[i]
#     if c=="a"or c=="e"or c=="i"or c=="o" or c=="u":
#         count+=1
# print(count,end="")

# #printing characters in index
# name="vigneswari"
# for i in range(len(name)):
#     print(name[i],"is in",i,"index")

# #printing vowels in index
# name="vigneswari"
# for i in range(len(name)):
#     c=name[i]
#     if c=="a"or c=="e" or c=="i" or c=="o" or c=="u":
#           print(name[i],"is in",i,"index")

# #counting no.of consonants in a string
# word="vigneswari"
# count=0
# for i in range(len(word)):
#     c=word[i]
#     if c!='a'and c!='e'and c!='i'and c!='o'and c!='u':
#         count+=1
# print(count)

# #converting string into uppercase
# word="vigneswari"
# word=word.upper()#making the whole string into uppercaase
# print(word)
# word="VIGNESWARI"
# word=word.lower()#making the whole string into lowercase
# print(word)
# word="vigneswari"
# word=word.capitalize()#the first letter should be capital
# print(word)
# sen="don't be sad,enjoy every moment"
# sen=sen.title()#all the words first letter into capital
# print(sen)

# #removing the spaces from starting and ending 
# sen=input("enter your name:")
# sen=sen.strip()#removing spaces starting and ending
# print(sen,len(sen))
# print(sen=="be yourself")

# #removing left spaces use lstrip()
# name=input("enter your name:")
# name=name.lstrip()
# print(name,len(name))
# print(name=="vigneswari")

# #removing left spaces use rstrip()
# name=input("enter your name:")
# name=name.rstrip()
# print(name,len(name))
# print(name=="vigneswari")

# #replace()
# name="hello world"
# name=name.replace("world","guys")
# print(name)
# name="hello world"
# name=name.replace("wo","guys")
# print(name)

# #find(),count()
# word="python is too good"
# print(word.find("t"))
# print(word.count("o"))

# #counting the no.of words in a string
# sen="i have one sweet and cute brother"
# spaces=sen.strip().count(" ")
# print("there are",spaces+1,"words")

# #checking wheather the given input is in uppercase or lowercase
# char=input("enter the char:")
# if char==char.upper():
#     print("char is in uppercase")
# else:
#     print("char is in lower case")

# #counting the  number of uppercase letters in a string
# sen="Not All heroes wear Caps Some wear Stethoscopes"
# count=0
# for i in range(len(sen)):
#     if sen[i]==sen[i].upper() and sen[i]!=" ":
#          count+=1
# print(count) 

# Create a string with your name and print it.
# name="vigneswari"
# print(name)

# Get the first character from the string.
# name="vigneswari"
# print(name[0])

# Get the last character from the string.
# name="vigneswari"
# s=len(name)-1
# print(name[s])

# Concatenate two strings.
# string1="Konidela Pawan Kalyan"
# string2="Deputy Chief Minister"
# print(string1+string2)
# print(string1+ " " +string2)

# Repeat a string 3 times
# name="Pawan Kalyan"
# print(name*3)

# Slice the first 5 characters.
# name="Pawan kalyan"
# print(name[0:5])

# Reverse a string using slicing.
# name="Pawan Kalyan"
# print(name[::-1])

# Check if a substring exists in a string.
# name="enjoy moment"
# sub_string="every"
# if sub_string in name:
#     print(sub_string,"exists")
# else:
#     print(sub_string,"not exists")

# Find the length of a string.
# name="pawan kalyan"
# print(len(name))

# Convert string to uppercase.
# name="pawan kalyan"
# name=name.upper()
# print(name)

# Convert string to lowercase.
# name="PAWAN KALYAN"
# name=name.lower()
# print(name)

# Capitalize the first letter.
# name="pawan kalyan"
# print(name.capitalize())

# Convert a string to title case.
# name="pawan kalyan"
# print(name.title())

# Remove leading spaces using lstrip().
# name=input("enter name:")
# print(name.lstrip())

# Remove trailing spaces using rstrip().
# name=input("enter name:")
# print(name.rstrip())

#startswith()
# name="pawan kalyan"
# print(name.startswith("p"))

#endswith()
# name="pawankalyan"
# print(name.endswith("d"))

#isalpha()
# name="pawankalyan"
# print(name.isalpha())

#isdigit()
# mobile="987654321"
# print(mobile.isdigit())

#isalnum()
# name="pawankalyan123"
# print(name.isalnum())

#swapcase()
# name="PawanKalyaN"
# print(name.swapcase())

#zfill()
# name="pawankalyan"
# print(name.zfill(15))

#split()
# name="pawan kalyan"
# print(name.split(" "))

#join()
# name=["he","is","my","idol"]
# print(" ".join(name))

#palindrome checking
# name="nayan"
# rev=""
# for i in range(len(name)-1,-1,-1):
#     rev+=name[i]
# if name==rev:
#         print("palindrome")
# else:
#         print("not a palindrome")

# Remove both ends’ spaces using strip().
# word=input("enter word:")
# print(word.strip(),len(word))

#Replace all spaces with underscores.
# word=input('enter word:')
# result=""

# for i in range(len(word)):
#     if word[i]==" ":
#         result+="_"
#     else:
#         print(word[i])
# print(result)

#Count how many times a character appears
# word="Hari hara veeramallu"
# print(word.count("r"))

#Find index of a character using find().
# word="vigneswari"
# print(word.find("s"))

#Use rfind() to find last occurrence.
# word="vigneswari"
# last=len(word)-1
# print(word[last])
# word="vigneswari"
# word=word.rstrip()
# print(word)

# Use index() to find substring position
# text = "laddu is sweet"
# position = text.index("is")
# print("Position:", position)

#Split a string by spaces
# string="vigneswari"
# string=list(string)
# separate=" ".join(string)
# print(separate)

# Join a list of words into a string.
# string=['i','am','a','fan','of','powerstar']
# print(" ".join(string))

#Check if string starts with "Hello"
# string="hello world"
# print(string.startswith("hello"))

#Check if string ends with "world"
# string="hello world"
# print(string.endswith("world"))

#Check if a string is digit.
# num="93980"
# print(num.isdigit())

#Check if a string is alphabet.
# name="pawankalyan"
# print(name.isalpha())

#Check if a string is alphanumeric.
# name="pawankalyan123"
# print(name.isalnum())

#Get ASCII value of a character
# character="V"
# print(ord(character))

#Convert ASCII to character.
# ascii=121
# print(chr(ascii))

#Remove punctuation from string.
# name="pawan.kalyan"
# res=""
# for i in range(len(name)):
#     if name[i].isalpha():
#         res+=name[i]
# print(res)


#Swap case of all characters
# name="pawankalyan"
# print(name.swapcase())

# Count total words in a string.
# sentence="believe yourself and give your best"
# spaces=sentence.strip().count(" ")
# print(spaces+1)

# Count total sentences in a string.



#Convert string to list of characters.
# sen="priyadarshini believe yourself"
# print(sen.split(" "))

# Convert list of characters to string
# list=['believe','yourself']
# print(" ".join(list))

#Pad string to the left with * to length 10
# string="ammu"
# print(string.rjust(10,"*"))

# Center align string using center()
# s="pawankalyan"
# print(s.center(10,"_"))

# Format string with variables using f-string.
# string="pawankalyan"
# print(f"{string},deputy cheif minister of Andhra Pradesh")

# Use % operator to format a string.
# name="swejan"
# age=10
# format="my name is %s and i am %d years old" % (name, age)
# print(format)
