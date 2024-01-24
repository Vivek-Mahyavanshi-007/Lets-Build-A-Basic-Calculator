# My Calculator

fh = open('Output.txt', 'w')

first = input("Enter first number : ")
second = input("Enter second number : ")

first = int(first)
second = int(second)

print("----press keys for operator (+,-,*,/,%)----")

operator = input("Enter operator : ")

result = 0

if operator == "+":
    print(first + second)
    result = first + second
elif operator == "-":
    print(first - second)
    result = first - second
elif operator == "*":
    print(first * second)
    result = first * second
elif operator == "/":
    print(first / second)
    result = first / second
elif operator == "%":
    print(first % second)
    result = first % second
else :
    print("Invalid Operation")
    fh.write(f"Invalid Operation")

# Write entered values and operation to the file
fh.write(f"Entered values: {first}, {second}\n")
fh.write(f"Operation: {first} {operator} {second}\n")
fh.write(f'Result = {result}')

fh.close()