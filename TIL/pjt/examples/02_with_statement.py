content = open('users.csv')
print(content)
print(content.read())

with open('example.txt', 'r') as file:
    print(file.read())

with open('users.csv', 'r') as file:
    print(file.read())

print(content.read())
print(file.read())