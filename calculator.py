#A simple calclulator program.

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

#Get users choice of operation and compute accordingly.

users_choice = int(input("Enter your choice (1-4): "))
if users_choice == 1:
    result= number1+number2
    operation = "+"
elif users_choice == 2:
    result= number1-number2
    operation = "-"
elif users_choice == 3:
    result= number1*number2
    operation = "*"
elif users_choice == 4:
    result= number1/number2 
    operation = "/"
else:
    print("Invalid choice!")

print(f"{number1} {operation} {number2} = {result}")
