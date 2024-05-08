"""
Task - 01
CALCULATOR APP
"""

# OPERATORS: +    -    *    /    %
import sys
n1 = int(input("Enter operand_1: "))
n2 = int(input("Enter a operand_2: "))
op = input("Enter a valid Operator")
result = 0

#switch case
match op:
    case '+':
        result = n1+n2
    case '-': 
        result = n1-n2
    case '*':
        result = n1*n2
    case '/':
        result = n1/n2
    case '%':
        result = n1%n2
    case _:                     # Default Case
        print("Invalid operator")
        sys.exit(1)
        
    
print("The result of ", n1, " ", op, " ", n2, " = ", result)

    

