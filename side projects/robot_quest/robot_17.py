# 빨강에서 로봇 멈추기 - until 사용
from hub import port
import motor_pair, color_sensor, color, runloop

motor_pair.pair(motor_pair.PAIR_1, port.E, port.F)

def is_color_red():
    return color_sensor.color(port.A) is color.RED

async def main():
    motor_pair.move_tank(motor_pair.PAIR_1, 300, 300)
    await runloop.until(is_color_red)
    motor_pair.stop(motor_pair.PAIR_1)
    print("RED!")
runloop.run(main())