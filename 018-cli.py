main_command_list = [
    '+: add numbers',
    '-: subtract numbers',
    '*: multiply numbers',
    '/: divide numbers',
    'q quit: quit'
]

def add(a, b):
    return a + b

def subtract(a, b):
    return a + b

operations = {
    "add": add,
    "subtract": subtract
}

while True:
    command = input('What do you want to do?\n' + '\n'.join(main_command_list) + '\n')
    operations.get(command, '')
    if command == '+':
        pass
    elif command == '-':
        pass
    elif command == '*':
        pass
    elif command == '/':
        pass
    elif command == 'q' or command == 'quit':
        break
    else:
        print("Command not found!")