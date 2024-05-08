"""
Task - 02
PASSWORD GENERATOR
"""
import random
password = ""


n = int(input("Enter the length of Password you want: "))
i = 0
diff = input("Enter the Difficulty level(H: hard, M: Medium, E: Easy) of your passward: ")
if (diff == 'H'):
    while i < n:
        letter = random.choice(",><?/\"':;{}[]-_=+-*/a0b1c2d3e4f5g6h7i8j9klmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ0142536789")
        password += letter
        i = i + 1
elif (diff == 'M'):
    while i < n:
        letter = random.choice("a0b1c2d3e4f5g6h7i8j9klmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        password += letter
        i = i + 1
else:
    while i < n:
        letter = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
        password += letter
        i = i + 1


print("Your Password is : \n", password)
