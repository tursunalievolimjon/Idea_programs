# English
# I didn't know the loop "while" when i created my "calculator" program first.
# So I've added changes to my "calculator" program after how i've learnt the loop "while".
# Uzbek
# Men "Calculator" dasturimni yaratganimda "while" tsikl-ni bilmas edim.
# Shuning uchun "while" tsikl-ni urganganimdan song dasturimni qayta ishga tushidigon qildim hamda o'zgartirishlar kiritdim.

while True:
    til = input('Tilni tanlang uzb/eng:')
    if til=='eng':
        formula = input('How do you want to calculate: plus, minus, multiplication, division ? :')
        if formula == 'plus':
            a = int(input('Enter the first number: '))
            b = int(input('Enter the second number: '))
            c = a + b
            print('Answer',c)
        elif formula == 'minus':
            a = int(input('Enter the first number: '))
            b = int(input('Enter the second number: '))
            c = a - b
            print('Answer',c)
        elif formula == 'multiplication':
            a = int(input('Enter the first number: '))
            b = int(input('Enter the second number: '))
            c = a * b
            print ('Answer',c)
        elif formula == 'division':
            a = int(input('Enter the first number: '))
            b = int(input('Enter the second number: '))
            c = a / b
            print('Answer',c)
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
            print('Choose one of the styles shown!')
            input()
            print('You can enter a character instead of a word')
            input()
            print('For example, you can enter the word plus with +')
            continue
        
    else:
        formula = input("Qanday hisoblashni hohlaysiz: plus, minus, kopaytiruv, boluv ? :")
        if formula == "plus":
            a = int(input("Birinchi sonni kiriting: "))
            b = int(input("Ikkinchi sonni kiriting: "))
            c = a + b
            print("Javob",c)
        elif formula == "minus":
            a = int(input("Birinchi sonni kiriting: "))
            b = int(input("Ikkinchi sonni kiriting: "))
            c = a - b
            print("Javob",c)
        elif formula == "kopaytiruv":
            a = int(input("Birinchi sonni kiriting: "))
            b = int(input("Ikkinchi sonni kiriting: "))
            c = a * b
            print ("Javob",c)
        elif formula == "boluv":
            a = int(input("Birinchi sonni kiriting: "))
            b = int(input("Ikkinchi sonni kiriting: "))
            c = a / b
            print("Javob",c)
        elif formula == '+':
            a = int(input("Birinchi sonni kiriting: "))
            b = int(input("Ikkinchi sonni kiriting: "))
            c = a + b
            print("Javob",c)
        elif formula == '-':
            a = int(input("Birinchi sonni kiriting: "))
            b = int(input("Ikkinchi sonni kiriting: "))
            c = a - b
            print("Javob",c)
        elif formula == '*':
            a = int(input("Birinchi sonni kiriting: "))
            b = int(input("Ikkinchi sonni kiriting: "))
            c = a * b
            print ("Javob",c)
        elif formula == '/':
            a = int(input("Birinchi sonni kiriting: "))
            b = int(input("Ikkinchi sonni kiriting: "))
            c = a / b
            print("Javob",c)
            
        else:
            print("Korsatilgan turlardan birini tanlang!")
            input()
            print("Sozlar urniga belgilar kiritishingiz mumkun")
            input()
            print("Misol uchun:plus sozini + bilan")
            continue
        
    # Davom ettirish yoki yoq
    if til=='eng':
        turn = input('Yes/No:')
        if turn =='No':
            break    
        else:
            continue
    else:
        turn = input('Xa/Yoq:')
        if turn =='Yoq':
            break
        else:
            continue