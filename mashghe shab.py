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
