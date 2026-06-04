num1 = float(input("First Number"))
num2 = float(input("Second Number"))
operation = (input("Operation?(+, -, *, /)"))


if operation == "+":
    result = num1 + num2
    print("Answer:", result)

if operation == "-":
    result = num1 - num2
    print("Answer:", result)

if operation == "*":
    result = num1 * num2
    print("Answer:", result)
    
if operation == "/":
    result = num1 / num2
    print("Answer:", result)