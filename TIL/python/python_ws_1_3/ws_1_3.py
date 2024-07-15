""" 
- 나이가 18세 이상인 사용자를 필터링하는 함수를 작성하시오.
- 활성화된(is_active가 True인) 사용자를 필터링하는 함수를 작성하시오.
- 나이가 18세 이상이고 활성화된 사용자를 필터링하는 함수를 작성하시오.
- 위의 함수를 별도의 모듈로 작성하고, 이를 메인 파일에서 불러와 사용하시오. 
"""

users = [
    {"username": "alice", "age": 25, "is_active": True},
    {"username": "bob", "age": 17, "is_active": False},
    {"username": "charlie", "age": 30, "is_active": True},
    {"username": "david", "age": 22, "is_active": False},
    {"username": "eve", "age": 29, "is_active": True}
]

def older_18(users):
    return [user for user in users if user['age'] >= 18]
""" 
def older_18(users):
    result = []
    for user in users:
        if user['age'] >= 18:
            result.append(user)
    return result
 """

def active_users(users):
    return [user for user in users if user['is_active']]

def older_18_active_users(users):
    return [user for user in users if user['age'] >= 18 and user['is_active']]

adults = older_18(users)
active_users = active_users(users)
adult_active_users = older_18_active_users(users)
print("Adults:", adults)
print("Active Users:", active_users)
print("Adult Active Users:", adult_active_users)