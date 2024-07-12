# curve turn을 하기 위해서는 왼쪽과 오른쪽 바퀴의 모터 속도가 서로 달라야합니다.

from hub import port
import motor_pair, runloop

motor_pair.pair(motor_pair.PAIR1, port.E, port.F)

async def main():
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 300, 100, 5000)

runloop.run(main())
