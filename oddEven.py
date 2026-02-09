def num(n):
 if n ==0:
   return "Zero"
 elif n%2 == 0:
   return "Even"
 else:
    return "Odd"
number = int(input("Enter a number: "))
print(num(number))
