import csv

with open('users.csv', 'r', encoding='utf-8') as file:
    #content = csv.reader(file)
    content = csv.DictReader(file)
    print(content)
    for row in content:
        print(row)