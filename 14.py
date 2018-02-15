given_string = list(input("Enter a String : "))
# print(given_string)   # test case
new = []
# given_string = given_string.split()
duplicate_word = list(input("Which element do you wanna remove : "))
# print(duplicate_word)  # test case
# duplicate_word = duplicate_word.split()
for duplicate_word in given_string:
    if duplicate_word not in new:
        new.append(duplicate_word)

print("After removing duplicates : "+''.join(new))