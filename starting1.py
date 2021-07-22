#the code below demostate an iterative way to calculate the factorial of a given number
number = int(input("Enter a number to find its factorial"))
factorial= 1
for i in range(1,number+1):
    factorial= factorial*i
print(factorial)
# next time we will learn how to find factorial of a number using recursive method.
