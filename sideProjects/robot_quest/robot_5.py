from hub import sound
import runloop
note = {'도':261, '레':293, '미':330, '파':349, '솔':392, '라':440, '시':493}

async def main():
    # 뽀로로 노래
    for i in range(3):
        await sound.beep(note['도'] * 2, 500)
        await sound.beep(note['라'], 500)
        await sound.beep(note['파'], 500)
        await sound.beep(note['솔'], 250)
        await sound.beep(note['솔'], 250)
        await sound.beep(note['도'], 500)
        await sound.beep(note['도'], 500)

runloop.run(main())