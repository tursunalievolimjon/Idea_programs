while True:
    a=int(input('Misoldagi a sonini kiriting:'))
    b=int(input('Misoldagi b sonini kiriting:'))
    c=int(input('Misoldagi c sonini kiriting:'))
    print('D=',b**2-4*a*c)
    d=b**2-4*a*c
    print('x(1)=',((-b+d)/2*a),'x(2)=',((-b-d)/2*a))