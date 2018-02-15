print("Enter an Integer : ")
number = int(input())
if number & 1:
    print("Number is Odd")
else: print("Number is Even")

if number%10 == 0 and number%50 == 0 and number%30 == 0:
    print("Divisible by 10, 50 and 30")
else:
    print("Is n't divisible by 10, 50 and 30")