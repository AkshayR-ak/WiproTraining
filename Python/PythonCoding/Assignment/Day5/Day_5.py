text = input('Enter text to save in a file:')
filename = 'output.txt'
with open(filename, 'w') as file:
    file.write(text)

with open(filename, 'r') as file:
    print('Output:')
    print(file.read())

