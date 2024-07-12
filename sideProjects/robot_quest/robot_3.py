import motor, runloop
from hub import port

async def main():
    velocity = 720

    await motor.run_for_degrees(port.E, 360, velocity)
    await motor.run_for_degrees(port.F, 360, velocity)

runloop.run(main())