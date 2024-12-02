def calculator():
    while True:
        try:
            print("Enter the first number:")
            a=int(input())
            print("Enter the second numbers")
            b=int(input())
            if(a==0 or b==0):
                print("Enter number greater than 0")
                continue
            break
        except ValueError:
            print("Enter valid input")
    print('''Operation to be performed
      Addition -'+'
      Subtraction -'-' 
      Division -'%'
      Multiplication-'*'
      ''')
    try:
        c=input()
        if (c=='+'):
            print("The output is:",a+b)
        elif(c=='-'):
            print("The output is:",a-b)
        elif(c=='*'):
            print("The output is:",a*b)
        elif(c=='%'):
            print("The output is:",a/b)
        else:
            print("Check symbol is valid .",c)             
    except Exception as e:
        print("Check the number.",e)
calculator()        


