b = list('')
for i in range(4):
    c = input("Enter "+ str(i+1) +" member of tuple : ")
    #b.append(list(input("Enter member of tuple : ")))
    b.append(c)
btup = tuple(b)
print(str(btup))
print()

