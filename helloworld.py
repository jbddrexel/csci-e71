from sys import argv

if len(argv) > 1:
    name = argv[1]
else:
    name = 'John'

print(f'Hello, {name}!')
