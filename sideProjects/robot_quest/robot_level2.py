""" 
###################################
#           1. 로켓 수송           #
###################################

from hub import port
import motor_pair, runloop

motor_pair.pair(motor_pair.PAIR_1, port.E, port.F)

async def main():
    # 80cm 전진
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 1620, 50, 50)
    await runloop.sleep_ms(2000)# 2초 대기

    # 80cm 후진
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 1620, -200, -200)

runloop.run(main()) 
"""

""" 
###############################
#       2. 암석 샘플 채취      #
###############################

from hub import port 
import runloop 
import motor_pair 
import color_sensor, color

motor_pair.pair(motor_pair.PAIR_1, port.E, port.F)


async def main(): 
    
    # 빨간색에서 멈춤
    while color_sensor.color(port.A) is not color.RED:
        if color_sensor.color(port.A) is not color.BLUE:
            motor_pair.move_tank(motor_pair.PAIR_1, 150, 50)
        else:
            motor_pair.move_tank(motor_pair.PAIR_1, 50, 150)

    motor_pair.stop(motor_pair.PAIR_1)
    
    # 360도 회전
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 360, 300, -300)
    await runloop.sleep_ms(2000)
    # await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 720, -300, 300)

    # 돌아가기
    while True:
        if color_sensor.color(port.A) is color.BLUE:
            motor_pair.move_tank(motor_pair.PAIR_1, 50, 150)
        else:
            motor_pair.move_tank(motor_pair.PAIR_1, 150, 50)


runloop.run(main())
"""


""" 
######################################
#       3. 깃발 게양 직선 이동으로     #
######################################

from hub import port
import motor_pair, motor, runloop, time

motor_pair.pair(motor_pair.PAIR_1, port.E, port.F)

# 바퀴 회전 각도 계산 (상수 값 사용)
distance_130cm = 2900 # 값 계속 바꿨음

# 로봇 팔을 내리는 함수
async def lower_arm():
    await motor.run_to_absolute_position(port.C, 120, 500, direction=motor.SHORTEST_PATH)

# 로봇 팔을 올리는 함수
async def raise_arm():
    await motor.run_to_absolute_position(port.C, 0, 500, direction=motor.SHORTEST_PATH)

async def main():
    # 로봇 팔을 올립니다 (시작 상태)
    await raise_arm()

    # 125cm 전진
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, distance_130cm, 300, 300)

    # 로봇 팔을 내립니다
    await lower_arm()

    # 125cm 후진
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, distance_130cm, -300, -300)

runloop.run(main())
"""

""" 
#########################
#   4. 거주 시설 야매    #
#########################

from hub import port 
import runloop 
import motor_pair 
import color_sensor, color

motor_pair.pair(motor_pair.PAIR_1, port.E, port.F)


async def main(): 
    
    # 빨간색에서 멈춤
    while color_sensor.color(port.A) is not color.RED:
        if color_sensor.color(port.A) is not color.BLUE:
            motor_pair.move_tank(motor_pair.PAIR_1, 150, 50)
        else:
            motor_pair.move_tank(motor_pair.PAIR_1, 50, 150)

    motor_pair.stop(motor_pair.PAIR_1)
    
    # 90도 회전
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 180, -300, 300)
    await runloop.sleep_ms(2000)

    # 빨간색에서 멈춤
    while color_sensor.color(port.A) is not color.RED:
        if color_sensor.color(port.A) is not color.BLUE:
            motor_pair.move_tank(motor_pair.PAIR_1, 150, 50)
        else:
            motor_pair.move_tank(motor_pair.PAIR_1, 50, 150)

    motor_pair.stop(motor_pair.PAIR_1)

    # 직진
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 450, 300, 300)

    # 후진
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, -450, 300, 300)

    # 90도 회전
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 180, -300, 300)
    await runloop.sleep_ms(2000)

    # 돌아가기
    while True:
        if color_sensor.color(port.A) is color.BLUE:
            motor_pair.move_tank(motor_pair.PAIR_1, 50, 150)
        else:
            motor_pair.move_tank(motor_pair.PAIR_1, 150, 50)


runloop.run(main()) 
"""