from Simpletimer import simpletimer
from BMP280 import BMP280 
timer1=simpletimer()

import board
#the default values of bmp bmp=BMP280(device_address=0x76,scl=board.GP5,sda=board.GP4,led_pin=board.GP25,sea_level_pressure=1017,temp_offset=-2.7)
bmp=BMP280(scl=board.GP5,sda=board.GP4)
bmp.print_current_settings()
while True:
    if(timer1.timer(2000)):
        [temperature,pressure,altitude]=bmp.read_all()
        print(f"temperature:{temperature:.2f}C \n\npressure:{pressure:.0f}hPa \n\naltitude:{altitude:.0f}m\n")
    bmp.blink(1000)
