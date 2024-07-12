from hub import port
import motor_pair, runloop

motor_pair.pair(motor_pair.PAIR_1, port.E, port.F)

async def main():

    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 360, 0)
    await runloop.sleep_ms(3000)
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, -360, 0, velocity=500)

runloop.run(main())