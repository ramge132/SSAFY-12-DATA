from hub import port
import color_sensor, time
# 컬러를 인식하면 콘솔에 색상 상수가 프린트 됩니다.

while True :
    time.sleep_ms(200)

    print(color_sensor.color(port.A))
    # Black (0)
    # Violet (1)
    # Blue (3)
    # Green (5)
    # Yellow (7)
    # Red (9)
    # White (10)
    # No color (-1)