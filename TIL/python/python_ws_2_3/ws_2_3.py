"""
- 3433번 문제에서 작성한 코드에서 이어서 작성한다.

- MovieTheater 클래스를 상속받는 VIPMovieTheater 클래스를 정의한다.
- VIPMovieTheater 클래스는 VIP 좌석 수를 저장하는 vip_seats 인스턴스 변수를 가진다.
    - 생성자에서 처리되어야 한다.
- VIPMovieTheater 클래스는 VIP 좌석을 예약하는 reserve_vip_seat 메서드를 가진다.
    - reserve_vip_seat 메서드는 예약 가능한 VIP 좌석이 있는 경우, vip_seats를 1 감소시키고 예약 성공 메시지를 반환한다.
    - 예약 가능한 VIP 좌석이 없는 경우, 예약 실패 메시지를 반환한다.
- VIPMovieTheater 클래스는 reserve_seat 메서드를 오버라이딩하여, VIP 좌석이 먼저 예약되도록 한다.
    - VIP 좌석이 예약 가능한 경우, reserve_vip_seat 메서드를 호출하여 VIP 좌석을 예약한다.
    - VIP 좌석이 예약 불가능한 경우, 부모 클래스의 reserve_seat 메서드를 호출하여 일반 좌석을 예약한다. 
"""

class MovieTheater:
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

class VIPMovieTheater(MovieTheater):
    def __init__(self, name, total_seats, vip_seats):
        super().__init__(name, total_seats)
        self.vip_seats = vip_seats

    def reserve_vip_seat(self):
        if self.vip_seats > 0:
            self.vip_seats -= 1
            return "VIP 좌석 예약이 완료되었습니다."
        else:
            return "예약 가능한 VIP 좌석이 없습니다."
        
    def reserve_seat(self):
        if self.vip_seats > 0:
            return self.reserve_vip_seat()
        else:
            return super().reserve_seat()

vip_megabox = VIPMovieTheater("VIP 메가박스", 1, 3)

print(vip_megabox.reserve_seat())
print(vip_megabox.reserve_seat())
print(vip_megabox.reserve_seat())
print(vip_megabox.reserve_seat())
print(vip_megabox.reserve_vip_seat())

