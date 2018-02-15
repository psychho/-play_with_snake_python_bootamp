# Find Solution of quadratic equation

import math

print("Enter coefficient of quadratic equation : ")
a = int(input())
b = int(input())
c = int(input())

d = math.sqrt((b**2 - 4*a*c))

sol1 = (-b + d)/2*a
sol2 = (-b - d)/2*a
# print("Solutions are : \n1st one {0}\n2nd one {1}".format(str(sol1),str(sol2)))
print("Solutions are \n")
print("1st one : %2.3f" %sol1)
print("2nd one : %2.3f" %sol2)

