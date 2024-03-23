num1 = float(input("Enter a number: "))
num2 = float(input("Enter second number: "))
op = input("Enter a operator:")

if op == "+":
    print(num1 + num2)
elif op == '-':
    print(num1-num2)
elif op == '*':
    print(num1 * num2)
elif op == "/":
    print(num1/num2)
else :
    print('invalid operator')