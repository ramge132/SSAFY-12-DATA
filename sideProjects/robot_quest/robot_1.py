from hub import light_matrix
from hub import sound
import runloop

async def main():
    # write your code here
    await sound.beep(550,2000)
    await light_matrix.write("Hi!")

runloop.run(main())