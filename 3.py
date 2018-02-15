#import math

print("Enter base number : ")
base = float(input())
print("Enter power of this number : ")
exponent = float(input())
#if True == isinstance(base, int) and isinstance(exponent, int) == True:
    #result = math.pow(int(base), int(exponent))
#    print("Result is : " + str(result))
#elif type(base) and type(exponent) == float:
 #   result = math.pow(float(base), float(exponent))
  #  print("Result is : " + str(result))
#elif type(base) == int and type(exponent) == float:
 #   result = math.pow(int(base), float(exponent))
  #  print("Result is : " + str(result))
#elif type(base) == float and type(exponent) == int:
 #   result = math.pow(float(base), int(exponent))
  #  print("Result is : " + str(result))


#result = math.pow(base,exponent)
result = base**exponent
print(result)