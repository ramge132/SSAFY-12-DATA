import csv
import requests
from pprint import pprint # import pprint만 하면 pprint.pprint를 해야함

URL = 'https://jsonplaceholder.typicode.com/todos/'
# response = requests.get(URL) # 첫번째 인자 = URL
# print(response) # <Response [200]> = status code임, 200은 정상동작이라는 뜻

response = requests.get(URL).json() # 첫번째 인자 = URL
print(response) # json 파일이 출력됨
print(type(response)) # json 파일과 타입<class 'list'>가 출력됨

# 내 서비스에 필요한 정보만 모아 놓은 리스트
completed_todo = []
# 내 서비스에 필요로 하는 필드 명
fields = ['id', 'title']
for item in response:
    # completed가 True인 경우만
    if item['completed']:
        # 모든 item을 순회하면서,
        # 새 리스트 competed_todo에 넣어야 됨
        # 내 서비스에 필요한 필드만 가진 새로운 dict
        temp_dict = {}
        for key in fields:
            temp_dict[key] = item[key]
            # print(temp_dict)
        completed_todo.append(temp_dict)

with open('completed_todos.csv', 'w', newline='', encoding='utf-8') as file:
    fieldsname = ['id', 'title']
    content = csv.DictWriter(file, fieldnames=fieldsname)

    content.writeheader()

    for item in completed_todo:
        # print(item)
        content.writerow(item)