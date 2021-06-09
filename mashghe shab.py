num1 = float(input('Enter number one\n'))
num2 = float(input('Enter number two\n'))
opration = input('''What do you want to do:\n + addition\n - subtraction
 * multiplication
 / division\n ''')
def calculator(addition):
    if opration == '+':
        print(f'addition is: {addition}')
addition = num1 + num2
calculator(addition)
def calculator(subtraction):
    if opration == '-':
        print(f'subtraction is: {subtraction}')
subtraction = num1 - num2
calculator(subtraction)
def calculator(multiplication):
    if opration == '*':
        print(f'multiplication is: {multiplication}')
multiplication = num1 * num2
calculator(multiplication)
def calculator(division):
    if opration == '/':
        print(f'division is: {division}')
division = num1 / num2
calculator(division)


###############################################################


command = input('che shekli mikhay?:\n')
if command == 'mosalas':
    def Perimeter_Area(mohit_mosalas, masahat_mosalas):
        if command2 == 'mohit':
            print(f'mohit mosavi ast ba: {mohit_mosalas}')
        elif command2 == 'masahat':
            print(f'masahat mosavi ast ba: {masahat_mosalas}')
        else:
            print('not found')
    command2 = input('mohit ya masahat?\n')
    ghaede = float(input('ghaede ra vared konid\n'))
    ertefa = float(input('ertefa ra vared konid\n'))
    mohit_mosalas = ghaede * 3
    masahat_mosalas = (ghaede * ertefa) / 2
    Perimeter_Area(mohit_mosalas, masahat_mosalas)
elif command == 'mostatil':
    def Perimeter_Area(mohit_mostatil, masahat_mostatil):
        if command2 == 'mohit':
            print(f'mohit mosavi ast ba: {mohit_mostatil}')
        elif command2 == 'masahat':
            print(f'masahat mosavi ast ba: {masahat_mostatil}')
        else:
            print('not found')
    command2 = input('mohit ya masahat?\n')
    tol = float(input('tol ra vared konid\n'))
    arz = float(input('arz ra vared konid\n'))
    mohit_mostatil = (tol + arz) * 2
    masahat_mostatil = tol * arz
    Perimeter_Area(mohit_mostatil, masahat_mostatil)
elif command == 'dayere':
        def Perimeter_Area(mohit_dayere, masahat_dayere):
            if command2 == 'mohit':
                print(f'mohit mosavi ast ba: {mohit_dayere}')
            elif command2 == 'masahat':
                print(f'masahat mosavi ast ba: {masahat_dayere}')
            else:
                print('not found')
        command2 = input('mohit ya masahat?\n')
        shoa = float(input('shoa ra vared konid\n'))
        mohit_dayere = (shoa * 2) * 3.14
        masahat_dayere = (shoa ** 2) * 3.14
        Perimeter_Area(mohit_dayere, masahat_dayere)
elif command == 'moraba':
    def Perimeter_Area(mohit_moraba, masahat_moraba):
        if command2 == 'mohit':
            print(f'mohit mosavi ast ba: {mohit_moraba}')
        elif command2 == 'masahat':
            print(f'masahat mosavi ast ba: {masahat_moraba}')
        else:
            print('not found')
    command2 = input('mohit ya masahat?\n')
    zele_moraba = float(input('zele moraba ra vared konid\n'))
    mohit_moraba = zele_moraba * 4
    masahat_moraba = zele_moraba ** 2
    Perimeter_Area(mohit_moraba, masahat_moraba)
else:
    print('not found')
