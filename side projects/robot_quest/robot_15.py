# 로봇 팔 움직이기
from hub import port
import runloop, motor

# C포트는 라지모터

# motor.run_to_absolute_position(port.C, 위치(각도), 라지모터속도범위(-1050~1050), 방향)

async def main():

    # 절대 위치 0까지 이동합니다(영점맞춤)
    await motor.run_to_absolute_position(port.C, 0, 100, direction=motor.CLOCKWISE)

    # 절대 위치 90으로 이동
    await motor.run_to_absolute_position(port.C, 90, 500, direction=motor.SHORTEST_PATH)

    await motor.run_to_absolute_position(port.C, 0, 100, -500) # 위

    await motor.run_to_absolute_position(port.C, 0, 110, 500) # 아래

runloop.run(main())