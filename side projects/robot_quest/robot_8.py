from hub import port
import runloop, motor_pair

motor_pair.pair(motor_pair.PAIR_1, port.E, port.F)

async def main():

    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 205, 300, 300)

# 계산:
# 바퀴 직경이 5.6cm이다.
# 그렇다면 2 * 3.14 * 2.8
# => 한 바퀴 이동하는데에 17.58

runloop.run(main())