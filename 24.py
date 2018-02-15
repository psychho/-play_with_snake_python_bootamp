import math

print(math.factorial(int(input("Enter an Integer : "))))

n = int(input("Enter another Integer : "))
result = 1
for i in range(1,n+1,1):
    result *= i
print("Factorial of "+str(n)+" is "+str(result))