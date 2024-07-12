# point turn, swing turn으로 칼같이 정확하게 90도 하려면 모터가 얼마나 회전해야하는가?

from hub import port
import motor_pair, runloop

motor_pair.pair(motor_pair.PAIR_1, port.E, port.F)

async def main():
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 360, 300, 300) # 직진
    
    # point turn으로 90도 회전
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 180, 300, -300)

    # swing turn으로 90도 회전 (왼쪽 바퀴 정지, 오른쪽 바퀴 회전)
    # 모터 각도=  90/360 × (축간 거리 × 360) / 바퀴의 원주​ = 90/360 × 12×360 / 17.6 ≈220.91도
    # await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 221, 300, 0)
    
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 360, 300, 300)
    
    
runloop.run(main())
