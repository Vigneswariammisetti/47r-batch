#using function return no of palindromes in a string
def no_of_palindromes(sentence):
    sentence=sentence.split()
    palindrome_exists=False
    count=0
    for i in range(len(sentence)):
        if sentence[i][::-1]==sentence[i]:
            palindrome_exists=True
            count+=1
    if palindrome_exists:
        print("There are",count,"palindromes")
    else:
         print("There are No Palindromes")
sentence=input("enter sentence:")
no_of_palindromes(sentence)

#CHECKING WHETHER THERE IS PALINDROMES OR NOT
# sen=input("enter sentence:")
# sen=sen.split()
# palindrome_exists=False
# for i in range(len(sen)):
#     if sen[i][::-1]==sen[i]:
#         palindrome_exists=True
#         print("there are palindromes")
#         break
# if palindrome_exists==False:
#     print("there are no palindromes")

#slicing
# string[start:stop:step]
# string="ShreyasIyer"
# print(string[0:5:2])

# string="shreyasiyer"
# print(string[len(string)-4:len(string)])

#negative indexing
# word="pawankalyan"
# print(word[-1:-12:-1])

# word="pawankalyan"
# print(word[::-1])

#palindrome check
# word="vigneswari"
# if word[::-1]==word:
#     print("palindrome")
# else:
#     print("not a palindrome")

#substring in a string
# word="HariHaraVeeramallu"
# sub_str="Hara"
# sub_len=len(sub_str)
# for i in range(len(word)):
#     part=word[i:i+sub_len]
#     if part==sub_str:
#         print(part,"is present in",word)
#         break

