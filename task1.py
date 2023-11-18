
def calci():
        x = float(input('Enter the first number: '))
        y = float(input('Enter the second number: '))
        op = input('Enter the operator: ')
        if op == '+':
            res = x+y
            print(str(x) + '+' + str(y) + '=' + str(res))
        elif op == '-':
            res = x-y
            print(str(x) + '-' + str(y) + '=' + str(res))
        elif op == '*':
            res = x*y
            print(str(x) + '*' + str(y) + '=' + str(res))
        elif op == '/':
            if y == 0:
                print('Division by zero error!')
            else:
                res = x/y
                print(str(x) + '/' + str(y) + '=' + str(res))


calci()
once_more = input('Do you wish to perform another calculation? (y/n): ')
if once_more.lower() == 'y':
    calci()
elif once_more.lower() == 'n':
    print('Thank you!')