import math
number1 = int(input('input first number: ')) #choose your number
sign = input('input "+" or "-" or "*" or "/" or "**" or "sqrt" : ')  #choose symbol
number2 = int(input('input second number: '))
if sign in ('+', '-', "*", "/", '**',"sqrt"):
 if sign == '+' or sign == '-' or sign == "*" or sign == "**" or sign == "sqrt":
     if sign == '+':
         print(number1 + number2)
         if sign == '*':
             print(number1 * number2)
             if sign == "/":
                 print(number1 / number2)
                 if sign == "**":
                     print(number1 ** number2)

     else:
         print(math.sqrt (number1/number2))
 else:
     print('Error')