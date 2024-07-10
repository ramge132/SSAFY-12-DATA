from hub import light_matrix
from hub import sound
import runloop

def text_merge(txt1, txt2):
    txt = str(txt1) + " " + str(txt2)
    return txt

async def main():
    # write your code here
    await sound.beep(550,2000)
    await light_matrix.write("Hi!")
    print(text_merge("hello", "monkey"))
    print(text_merge("hello", "1000"))

runloop.run(main())