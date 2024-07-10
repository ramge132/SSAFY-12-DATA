from hub import port
import motor_pair, runloop

motor_pair.pair(motor_pair.PAIR_1, port.E, port.F)

async def main():

    motor_pair.move(motor_pair.PAIR_1,0) # 조향 모드 범위는 -100~100 , 0 = 직진
    await runloop.sleep_ms(2000)
    motor_pair.stop(motor_pair.PAIR_1)

runloop.run(main())