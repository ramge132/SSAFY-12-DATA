""" 
- 'Theater' 부모 클래스를 정의한다.
- 'Theater' 클래스는 영화관의 이름을 저장하는 'name' 인스턴스 변수를 가진다.
- 'Theater' 클래스는 영화관의 총 좌석 수를 저장하는 'total_seats' 인스턴스 변수를 가진다.
- 'Theater' 클래스는 현재 예약된 좌석 수를 저장하는 'reserved_seats' 인스턴스 변수를 가진다.
- 'Theater' 클래스는 좌석을 예약하는 'reserve_seat' 인스턴스 메서드를 가진다.
    - 'reserve_seat' 메서드는 예약 가능한 좌석이 있는 경우, 'reserved_seats'를 1 증가시키고 예약 성공 메시지를 반환한다.
    - 예약 가능한 좌석이 없는 경우, 예약 실패 메시지를 반환한다.

- MovieTheater 자식 클래스를 정의하고, Theater 클래스를 상속받는다.
- MovieTheater 클래스는 영화관의 총 영화 수를 저장하는 total_movies 클래스 변수를 가진다.
- MovieTheater 클래스는 영화관의 총 영화 수를 증가시키는 add_movie 클래스 메서드를 가진다.
    - add_movie 메서드는 total_movies를 1 증가시키고, 영화 추가 성공 메시지를 반환한다.
- MovieTheater 클래스는 영화관의 정보를 출력하는 description 정적 메서드를 가진다.
    - description 메서드는 영화관의 이름, 총 좌석 수, 예약된 좌석 수, 총 영화 수를 출력한다. 
"""

# Theater 부모 클래스 정의
class Theater:
    def __init__(self, name, total_seats):
        self.name = name
        self.total_seats = total_seats
        self.reserved_seats = 0

    # 좌석 예약 메서드 정의
    def reserve_seat(self):
        if self.reserved_seats < self.total_seats:
            self.reserved_seats += 1
            return "좌석 예약이 완료되었습니다."
        else:
            return "예약 가능한 좌석이 없습니다."

# MovieTheater 자식 클래스 정의 (Theater 상속)
class MovieTheater(Theater):
    total_movies = 0  # 클래스 변수로 총 영화 수를 추가

    # 영화 추가 클래스 메서드 정의
    @classmethod
    def add_movie(cls):
        cls.total_movies += 1
        return "영화가 성공적으로 추가되었습니다."

    # 영화관 정보 출력 정적 메서드 정의
    @staticmethod
    def description(theater):
        print(f"영화관 이름: {theater.name}")
        print(f"총 좌석 수: {theater.total_seats}")
        print(f"예약된 좌석 수: {theater.reserved_seats}")
        print(f"총 영화 수: {MovieTheater.total_movies}")

# MovieTheater 인스턴스 생성
megabox = MovieTheater("메가박스", 100)

# 좌석 예약 및 상태 확인
print(megabox.reserve_seat())
print(megabox.reserve_seat())

# 영화 추가
print(MovieTheater.add_movie())

# 영화관 정보 출력
MovieTheater.description(megabox)
