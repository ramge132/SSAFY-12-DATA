from hub import port
import runloop, motor_pair

motor_pair.pair(motor_pair.PAIR_1, port.E, port.F)

async def main():

    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 360,300,300)
    await runloop.sleep_ms(3000)
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, -360,300,300)