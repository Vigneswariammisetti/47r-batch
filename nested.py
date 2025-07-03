
#* * * * *
#* * * * *
#* * * * *
#* * * * *
#* * * * *
# rows=5
# for i in range(1,rows+1):#first loop will always be for row
#     pattern=""#for storing stars
#     for j in range(1,rows+1):
#         pattern += "*"+ " "
#     print(pattern)

# *
# * *
# * * *
# * * * *
# * * * * *
# rows=5
# for i in range(1,rows+1):
#     pattern=""
#     for j in range(1,i+1):
#         pattern+="*"+" "
#     print(pattern)



# 1 
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# rows=5
# for i in range(1,rows+1):
#     pattern=""
#     for j in range(1,i+1):
#         pattern+=str(j)+" "
#     print(pattern)


# 1 
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# rows=5
# for i in range(1,rows+1):
#     pattern=""
#     for j in range(1,i+1):
#         pattern+=str(i)+" "
#     print(pattern)

# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14
# rows=5
# num=1
# for i in range(1,rows+1):
#     pattern=""
#     for j in range(1,i+1):
#         pattern+=str(num)+" "
#         num+=1
#     print(pattern)

# rows=5
# for row in range(rows):
#     res="" 
#     for col in range(row+1):
#         res+=str(rows)+"  "
#     rows=rows-1
#     print(res)

# 5 5 5 5 5 
# 4 4 4 4
# 3 3 3
# 2 2 
# 1

# rows=5
# for i in range(rows,0,-1):
#     pattern=""
#     for j in range(1,i+1):
#         pattern+=str(i)+" "
#     print(pattern)

# * * * * *
# *       *
# *       *
# *       *
# * * * * *

# rows=5
# for i in range(1,rows+1):
#     pattern=""
#     for j in range(1,rows+1):
#         if i==1 or i==5 or j==1 or j==5:
#             pattern+="*"+" "
#         else:
#             pattern+=" "+" "#one space is for character and other space is for space between character
#     print(pattern)

# * * * * *
# *       
# *       
# *       
# * * * * *
rows=5
# for i in range(1,rows+1):
#     pattern=""
#     for j in range(1,rows+1):
#         if i==1 or i==5 or j==1:
#             pattern+="*"+" "
#     print(pattern)

# * * * * *
# *       
# * * * * *     
# *       
# * * * * *
# rows=7
# for i in range(1,rows+1):
#     pattern=""
#     for j in range(1,rows+1):
#         if i==1 or i==rows or j==1 or i==(rows//2)+1:
#             pattern+="*"+" "
#     print(pattern)

# * * * * *
#     *       
#     *       
#     *       
# * * * * *
# rows=7
# for i in range(1,rows+1):
#     pattern=""
#     for j in range(1,rows+1):
#         if i==1 or i==rows or j==(rows//2)+1 :
#             pattern+="*"+" "
#         else:
#             pattern+=" "+" "
#     print(pattern)

# rows=5
# for i in range(1,rows+1):
#     pattern=""
#     for j in range(1,rows+1):
#         if i==j or i+j==rows+1:
#             pattern+="*"+" "
#         else:
#             pattern+=" "+" "
#     print(pattern)

# rows=5
# for i in range(1,rows+1):
#     pattern=""
#     for j in range(1,rows+1):
#         if j==1 or j==rows or i==(rows//2)+1:
#             pattern+="*"+" "
#         else:
#             pattern+=" "+" "
#     print(pattern)

# rows=7
# for i in range(1,rows+1):
#     pattern=""
#     for j in range(1,rows+1):
#         if i==1 or j==(rows//2)+1:
#             pattern+="*"+" "
#         else:
#             pattern+=" "+" "
#     print(pattern)

# rows=7
# for i in range(1,rows+1):
#     pattern=""
#     for j in range(1,rows+1):
#         if j==1 or j==rows or i==j:
#             pattern+="*"+" "
#         else:
#             pattern+=" "+" "
#     print(pattern)

rows=7
for i in range(1,rows+1):
    pattern=""
    for j in range(1,rows+1):
        if i==1 or i==rows or i+j==rows+1:
            pattern+="*"+" "
        else:
            pattern+=" "+" "
    print(pattern)