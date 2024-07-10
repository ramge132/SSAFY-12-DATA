from hub import port
import motor_pair, runloop

# point turn하기 위해서는 왼쪽가 오른족 바퀴의 모터의 방향은 다르고 속도는 같아야 합니다.
motor_pair.pair(motor_pair.PAIR_1, port.E, port.F)

async def main():

    # 로봇이 720도 만큼 왼쪽모터 300, 오른쪽 모터 -300 속도로 움직입니다.
    # 모터가 서로 반대로 회전하기 때문에 point turn 합니다.
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 720, 300, -300)
    await runloop.sleep_ms(2000)
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 720, -300, 300)

runloop.run(main())