import math
x = float(input("Number one:"))
y = float(input("Number two:"))
operation = input("Operation:")
result = None

if operation == '+':
    result = x + y
elif operation == '-':
    result = x - y
elif operation == '*':
    result = x * y
elif operation == '/':
    result = x / y
elif operation == '**':
    result = x ** y
elif operation == '^': #anything
    result = math.sqrt(x)
if result is not None:
    print(result)
