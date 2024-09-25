valid = False

while not valid:
    try:
        x = int(input('enter a number: '))
        while x%2==0:
            print('bye')
        valid == True
    except ValueError as e:
        print('only enter a number.')
 