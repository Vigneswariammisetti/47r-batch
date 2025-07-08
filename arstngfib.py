# ARMSTRONG:sum of digits raised to the power (no.of digits)==number
# 153=no.of digits in 153 is 3 ,so the power should be 3
#     1**3+5**3+3**3
#     3+125+27
#     =153    IS AN ARMSTRONG NUMBER
def is_armstrong(num):
    temp = num
    result = 0
    n = len(str(num))                    # Convert number to string to easily find number of digits
    while temp > 0:                      #Calculate sum of digits raised to the power of num_digits
        digit = temp % 10
        result += digit ** n
        temp //= 10
    return result == num
number = int(input("Enter a number: "))
if is_armstrong(number):
    print(number, "is an Armstrong number.")
else:
    print(number, "is not an Armstrong number.")


#FIBONACCI SERIES:A sequence where each number is the sum of the two preceding ones:
n=52
a=0             #series always starts with 0 and 1
b=1
for i in range(n-1):
    c=a+b
    a=b
    b=c
print(a)



