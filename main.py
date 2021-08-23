from Simpletimer import simpletimer
from BMP280 import BMP280 
timer1=simpletimer()


bmp=BMP280()

while True:
    if(timer1.timer(2000)):
        [temperature,pressure,altitude]=bmp.read_all()
        print(f"temperature:{temperature:.2f}C \n\npressure:{pressure:.0f}hPa \n\naltitude:{altitude:.0f}m\n")
    bmp.blink(100)
