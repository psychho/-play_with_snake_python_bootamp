b = []
b1 = []
for i in range(5):
    c = input('Enter no. ' + str(i + 1) + ' member of 1st list : ')
    # b.append(list(input("Enter member of tuple : ")))
    b.append(c)
b[2] = input("Input to replace third element of this list : ")

for i in range(3):
    b1er = input('Enter no. ' + str(i + 1) + ' member of 2nd list : ')
    # b.append(list(input("Enter member of tuple : ")))
    b1.append(b1er)

final_list_is = b + b1
print("Sum of two list are : "+ str(final_list_is))