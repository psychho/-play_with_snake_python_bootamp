print("Enter to check whether palindrome or not : ")
in_string = input()
b = in_string[::-1]
if in_string == b :
    print("Is palindrome")
else: print("Is not a palindrome")