try:
    num1, num2 = eval(input('enter a two numbers seperated by a comma: '))
    x = num1/num2
    print('x')
except ZeroDivisionError as e:
    print('PASS A VALUE OTHER THAN ZERO!')
except SyntaxError as e:
    print('there is a syntax error.')
except:
    print('invalid error')
else:
    print('no error')
finally:
    print('this will get printed no matter what...:)')