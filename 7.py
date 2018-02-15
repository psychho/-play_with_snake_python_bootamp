print("Enter a number : ")
number = input()
a = str.isdigit(number)
count = 0
if a:
    while number != 0:
        number = int(number)
        number = number // 10
        count += 1
else: print("Input only Number")

print("Digits : " + str(count))

#or

"""print("Enter a number : ")
number = int(input())
count = 0

while number != 0:
    number = number//10
    count += 1
print("Digits : "+str(count))"""



#or

"""a = input()
b = len(a)
print(str(b))"""

