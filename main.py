import os
import calculator_art

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def devide(n1,n2):
    return n1 / n2

operation = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : devide
    }

def calculator():
    print(calculator_art.logo)
    num1 = float(input("What is the first number ? : "))
    for symbol in operation:
        print(symbol)
    in_program = True

    while in_program == True:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operation[operation_symbol]
        answer = calculation_function(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        print("")
        continue_operation = input("Do you want to continue ? \n<<<Type any key to quit>>>\nType 'yes' or 'no': \n").lower()
        
        if  continue_operation == "yes":
            num1 = answer
            
        elif continue_operation == 'no':
            in_program = False
            clear_screen()
            calculator()
        else:
            print("Program End.")
            in_program = False
calculator()
            
