# English
# I created my first program "Calculator" and you can calculate your easy examplples and tasks in this program.
# But there is a minus that you should launch this program again after you finish your calculating.
# Uzbek
# Men uzimning birinchi "Calculator" dasturimni yaratdim va siz bu dasturda sodda misollar-ni hisoblashingiz mumkun.
# Lekin bu dasturimda bitta kamchilik bor, har-bitta hisoblashdan song dasturni qayta ishga tushurishingiz kerak boladi.

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