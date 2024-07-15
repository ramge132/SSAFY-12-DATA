""" 
- User 클래스를 정의한다.
- User의 인스턴스 수를 기록할 수 있는 클래스 변수 user_count를 정의하고, 0을 할당한다.
- 생성자 메서드를 정의한다.
    - 생성자 메서드는 사용자의 이름과 이메일을 인자로 받는다.
    - 각 인스턴스는 고유한 이름과 이메일을 담을 수 있는 name과 email 변수를 가지고, 인자로 넘겨받은 값을 할당 받는다.
    - 인스턴스가 생성될 때마다 user_count가 1 증가해야 한다.
- 'SNS 사용자'에 대한 설명을 출력하는 description 스태틱 메서드를 정의한다.
- 2개 이상의 인스턴스를 생성하고, 각 인스턴스의 name과 email을 출력한다.
- User 클래스의 user_count를 출력한다.
- description 스태틱 메서드를 호출한다.
"""

# User 클래스 정의
class User:
    # 클래스 변수 정의
    user_count = 0

    # 생성자 메서드 정의
    def __init__(self, name, email):
        self.name = name
        self.email = email
        User.user_count += 1

    # SNS 사용자 설명 정적 메서드 정의
    @staticmethod
    def description():
        print("SNS 사용자는 소셜 네트워크 서비스를 이용하는 사람을 의미합니다.")

# 인스턴스 생성
user1 = User("Alice", "alice@example.com")
user2 = User("Bob", "bob@example.com")

# 각 인스턴스의 name과 email 출력
print(user1.name)
print(user1.email)
print(user2.name)
print(user2.email)

# 총 생성된 User 수 출력
print(f"현재까지 생성된 사용자 수: {User.user_count}")

# description 스태틱 메서드 호출
User.description()
