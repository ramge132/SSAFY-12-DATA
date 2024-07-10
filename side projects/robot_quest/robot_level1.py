##########################
#   우주 고속도로 주행    #
##########################

from hub import light_matrix 
from hub import sound 
from hub import port 
import motor 
import runloop 
import motor_pair 
import color_sensor, color, time

motor_pair.pair(motor_pair.PAIR_1, port.E, port.F)

def is_color_red(): return color_sensor.color(port.A) is color.RED

async def main(): 
    while True: 
        if color_sensor.color(port.A) is not color.BLACK: 
            motor_pair.move_tank(motor_pair.PAIR_1, 50, 150) 
        else: 
            motor_pair.move_tank(motor_pair.PAIR_1, 150, 50)

runloop.run(main()) 
