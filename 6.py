print("Input a Number 1 : ")
num1 = int(input())
print("Input a Number 2 : ")
num2 = int(input())
print("Input a Number 3 : ")
num3 = int(input())

if num1>=num2 and num1>=num3:
    maximum = num1
elif num2>=num1 and num2>=num3:
    maximum = num2
else :
    maximum = num3
print("Largest Number is : "+ str(maximum))
