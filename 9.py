in_string = input("Input a String : ")
vowel = []
consonant = []
for letters in in_string:
    if letters == 'a' or letters == 'e' or letters == 'i' or letters == 'o' or letters == 'u' :
        vowel.append(letters)
    else: consonant.append(letters)
len_vowel = len(vowel)
len_consonant = len(consonant)
space = in_string.count(' ')
actual_consonant = len_consonant-space

print("Vowels : {0}\nConsonant : {1} ".format(len_vowel,actual_consonant))