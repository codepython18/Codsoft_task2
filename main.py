print("Please select operation -\n" \
        "1. Addition\n" \
        "2. Subtraction\n" \
        "3. Multiplication\n" \
        "4. Division\n")

sel = int(input("Select operations form 1, 2, 3, 4 : "))
 
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

def addition(n1, n2):
    return n1 + n2
def subtraction(n1, n2):
    return n1 - n2
def multiplication(n1, n2):
    return n1 * n2
def division(n1, n2):
    return n1 / n2
 

 
if sel == 1:
    print("The answer of operation is ", number1, "+", number2, "=",
                    addition(number1, number2))
 
elif sel == 2:
    print("The answer of operation is ",number1, "-", number2, "=",
                    subtraction(number1, number2))
 
elif sel == 3:
    print("The answer of operation is ",number1, "*", number2, "=",
                    multiplication(number1, number2))
 
elif sel == 4:
    print("The answer of operationa1 is ",number1, "/", number2, "=",
                    division(number1, number2))
else:
    print("Invalid")