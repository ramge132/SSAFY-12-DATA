import motor_pair

from hub import port
# 포트 E와 F의 모터를 페어링 합니다.
# 왼쪽 모터는 E, 오른쪽 모터는 F

# 미디엄 모터 속도 범위는 -1110 ~ 1110
# 라지 모터 속도 범위는 -1050 ~ 1050

motor_pair.pair(motor_pair.PAIR_1, port.E, port.F)

