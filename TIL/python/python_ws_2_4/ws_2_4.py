""" 
- 3433번 문제에서 작성한 코드에서 이어서 작성한다.

- MovieTheater 클래스는 영화관의 총 영화 수를 증가시키는 add_movie 클래스 메서드를 가진다.
    - add_movie 메서드는 total_movies를 1 증가시키고, 영화 추가 성공 메시지를 반환한다.
- MovieTheater 클래스는 영화관의 정보를 출력하는 description 정적 메서드를 가진다.
    - description 메서드는 아래 문장을 출력한다.
    - '"이 클래스는 영화관의 정보를 관리하고 좌석 예약 및 영화 추가 기능을 제공합니다."
    - "영화관의 이름, 총 좌석 수, 예약된 좌석 수, 총 영화 수를 관리합니다."
"""

class MovieTheater:
    total_movies = 0

    def __init__(self, name, total_seats):
        self.name = name
        self.total_seats = total_seats
        self.reserved_seats = 0
    
    def __str__(self):
        return self.name
    
    def reserve_seat(self):
        if self.reserved_seats < self.total_seats:
            self.reserved_seats += 1
            return "좌석 예약이 완료되었습니다."
        else:
            return "잔여 좌석이 없어 예약에 실패했습니다."
    
    def current_status(self):
        print(f"총 좌석 수 : {self.total_seats}")
        print(f"예약된 좌석 수 : {self.reserved_seats}")

    @classmethod
    def add_movie(cls):
        cls.total_movies += 1
        return "영화가 성공적으로 추가되었습니다."
    
    @staticmethod
    def description():
        print("이 클래스는 영화관의 정보를 관리하고 좌석 예약 및 영화 추가 기능을 제공합니다.")
        print("영화관의 이름, 총 좌석 수, 예약된 좌석 수, 총 영화 수를 관리합니다.")
    
# MovieTheater 인스턴스 생성
megabox = MovieTheater("메가박스", 100)
cgv = MovieTheater("CGV", 150)

# 좌석 예약 및 상태 확인
print(megabox.reserve_seat())
print(megabox.reserve_seat())
print(cgv.reserve_seat())

# 영화 추가
print(MovieTheater.add_movie())
print(MovieTheater.add_movie())

# 현재 예약 상태 출력
megabox.current_status()
cgv.current_status()

# 영화관 정보 출력
print(f"총 영화 수: {MovieTheater.total_movies}")

# 클래스 설명 출력
MovieTheater.description()
