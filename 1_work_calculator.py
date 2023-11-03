formula = input("How do you want to calculate: plus, minus, multiplication, division ? :")
if formula == "plus":
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    c = a + b
    print("Answer",c)
elif formula == "minus":
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    c = a - b
    print("Answer",c)
elif formula == "multiplication":
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    c = a * b
    print ("Answer",c)
elif formula == "division":
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    c = a / b
    print("Answer",c)
elif formula == "+":
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    c = a + b
    print("Answer",c)
elif formula == "-":
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    c = a - b
    print ("Answer",c)
elif formula == "*":
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    c = a * b
    print("Answer",c)
elif formula == "/":
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    c = a / b
    print("Answer",c)

else:
    print("Choose one of the styles shown!")
    input()
    print("You can enter a character instead of a word")
    input()
    print("For example, you can enter the word plus with +")
input()
