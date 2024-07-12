# 검정색 선을 따라가다가 빨간색을 만나면 멈춥니다.

from hub import port
import motor_pair, color_sensor, color, runloop

motor_pair.pair(motor_pair.PAIR_1, port.E, port.F)


async def main():
    while color_sensor.color(port.A) is not color.RED:
        if color_sensor.color(port.A) is color.BLACK:
            motor_pair.move_tank(motor_pair.PAIR_1, 300, 150)
        else:
            motor_pair.move_tank(motor_pair.PAIR_1, 150, 300)
        motor_pair.stop(motor_pair.PAIR_1)
runloop.run(main())
