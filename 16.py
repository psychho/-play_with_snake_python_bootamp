b = list('')
for i in range(4):
    c = input('Enter no. ' + str(i + 1) + ' member of tuple : ')
    # b.append(list(input("Enter member of tuple : ")))
    b.append(c)
btup = tuple(b)
print("Tuple : "+ str(btup))

print("List : "+ str(list(btup)))
print()
