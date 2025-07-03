# printing numbers from 1 to 10 using function
def numbers():
    for i in range(1,11):
        print(i)
numbers()

# printing numbers from 10 to 1 in reverse order using fuction
def numbers():
    for i in range(10,0,-1):
        print(i)
numbers()

# printing all even numbers from 1 to 20 using function
def even():
    for i in range(0,21,2):
        print(i)
even()

# printing all odd numbers from 1 to 15 using function
def odd():
    for i in range(1,16):
        if i%2!=0:
            print(i)
odd()

# print multiplication table of 5
def table(n):
    for i in range(1,11):
        res=n*i
        print(n,"*",i, "=", res)
table(5)

# sum of numbers from 1 to 100
def total():
    count=0
    for i in range(0,101):
        count=count+i
        print(count)
total()

# square of numbers from 1 to 10 using function
def square_of_num():
    for i in range(1,11):
        square=i**2
        print(square)
square_of_num()

# cube of numbers from 1 to 5 using function
def cube_of_num():
    for i in range(1,6):
        cube=i**3
        print(cube)
cube_of_num()

# sum of even numbers from 1 to 50
def sum_of_even_num():
    total=0
    for i in range(1,51):
        if i%2==0:
            total=total+i
            i=i+1
    return total
print(sum_of_even_num())

# product of numbers from 1 to 5 using function
def product():
    result=1
    for i in range(1,6):
        result=result*i
        print(result)
product()