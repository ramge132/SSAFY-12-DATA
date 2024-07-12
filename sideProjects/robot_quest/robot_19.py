# 20cm보다 가까우면 정지, 먼 경우 직진
from hub import port
import motor_pair, distance_sensor, time
motor_pair.pair(motor_pair.PAIR_1, port.E, port.F)


while True:
    distance = distance_sensor.distance(port.B)
    if distance <200:
        motor_pair.stop(motor_pair.PAIR_1)
    else:
        motor_pair.move(motor_pair.PAIR_1, 0)
    time.sleep_ms(200)

