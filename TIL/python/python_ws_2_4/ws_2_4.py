""" 
- 3433번 문제에서 작성한 코드에서 이어서 작성한다.

- MovieTheater 클래스는 영화관의 총 영화 수를 증가시키는 add_movie 클래스 메서드를 가진다.
    - add_movie 메서드는 total_movies를 1 증가시키고, 영화 추가 성공 메시지를 반환한다.
- MovieTheater 클래스는 영화관의 정보를 출력하는 description 정적 메서드를 가진다.
    - description 메서드는 영화관의 이름, 총 좌석 수, 예약된 좌석 수, 총 영화 수를 출력한다.
"""

# MovieTheater 클래스 정의
class MovieTheater:
    total_movies = 0  # 클래스 변수로 총 영화 수를 추가

    def __init__(self, name, total_seats):
        self.name = name
        self.total_seats = total_seats
        self.reserved_seats = 0

    def __str__(self):
        return self.name

    # 좌석 예약 메서드 정의
    def reserve_seat(self):
        if self.reserved_seats < self.total_seats:
            self.reserved_seats += 1
            return "좌석 예약이 성공적으로 완료되었습니다."
        else:
            return "예약 가능한 좌석이 없습니다."

    # 현재 예약 상태 출력 메서드 정의
    def current_status(self):
        print(f"{self.name} 영화관의 총 좌석 수: {self.total_seats}")
        print(f"{self.name} 영화관의 예약된 좌석 수: {self.reserved_seats}")

    # 영화 추가 클래스 메서드 정의
    @classmethod
    def add_movie(cls):
        cls.total_movies += 1
        return "영화가 성공적으로 추가되었습니다."

    # 영화관 정보 출력 정적 메서드 정의
    @staticmethod
    def description():
        print("이 클래스는 영화관의 정보를 관리하고 좌석 예약 및 영화 추가 기능을 제공합니다.")
        print("영화관의 이름, 총 좌석 수, 예약된 좌석 수, 총 영화 수를 관리합니다.")

# VIPMovieTheater 클래스 정의 (MovieTheater 상속)
class VIPMovieTheater(MovieTheater):
    def __init__(self, name, total_seats, vip_seats):
        super().__init__(name, total_seats)
        self.vip_seats = vip_seats

    # VIP 좌석 예약 메서드 정의
    def reserve_vip_seat(self):
        if self.vip_seats > 0:
            self.vip_seats -= 1
            return "VIP 좌석 예약이 완료되었습니다."
        else:
            return "예약 가능한 VIP 좌석이 없습니다."

    # 일반 좌석 예약 메서드 오버라이딩
    def reserve_seat(self):
        if self.vip_seats > 0:
            return self.reserve_vip_seat()
        else:
            return super().reserve_seat()

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
