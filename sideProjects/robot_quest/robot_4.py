from hub import port
import motor, runloop

velocity = 450

async def main():
    global velocity

    degrees = 360

    for i in range(4):

        velocity = velocity + i * 90
        await motor.run_for_degrees(port.E, degrees, velocity)
        await motor.run_for_degrees(port.F, degrees, velocity)

runloop.run(main())
