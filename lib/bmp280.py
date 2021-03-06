import time

import board
from Simpletimer import simpletimer

import busio
import adafruit_bmp280


from digitalio import DigitalInOut, Direction, Pull


class BMP280:
    def __init__(self,device_address=0x76,scl=board.GP5,sda=board.GP4,led_pin=board.GP25,sea_level_pressure=1017,temp_offset=-2.7):
        self.device_address=device_address
        self.temp_offset=temp_offset
        self.ledpin=led_pin
        self.led = DigitalInOut(self.ledpin)
        self.led.direction = Direction.OUTPUT
        self.timer1 = simpletimer()
        self.timer2 = simpletimer()
        self.SCL = scl
        self.SDA = sda
        self.i2c = busio.I2C(scl=self.SCL, sda=self.SDA)
        self.bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(
            self.i2c, address=device_address)
        # change this to match the location's pressure (hPa) at sea level
        self.bmp280.sea_level_pressure = sea_level_pressure
    def print_current_settings(self):
        self.current_settings=[self.bmp280.sea_level_pressure, self.SCL,self.SDA,self.temp_offset,self.device_address]
        print(f"location sea level pressure:{self.bmp280.sea_level_pressure}\nselected SCL pin:{self.SCL}\nselected SDA pin:{self.SDA}\ntemperature offset:{self.temp_offset}\ndevice adress:{hex(self.device_address)}")
    
    def blink(self, delay_=500):
        if self.timer2.timer(delay_):
            self.led.value = not self.led.value
            #print(f"led state is:{led.value}")
    def start_print_loop(self,print_refresh=2000,blink_refresh=300):
        while True:
            if self.timer1.timer(print_refresh):
                self.temperature = self.bmp280.temperature+self.temp_offset
                print("\nTemperature: %0.1f C" % self.temperature)
                print("Pressure: %0.1f hPa" % self.bmp280.pressure)
                print("Altitude = %0.2f meters" % self.bmp280.altitude)
            self.blink(blink_refresh)
    def read_and_print_sensor(self):
        self.temperature = self.bmp280.temperature+self.temp_offset
        print("\nTemperature: %0.1f C" % self.temperature)
        print("Pressure: %0.1f hPa" % self.bmp280.pressure)
        print("Altitude = %0.2f meters" % self.bmp280.altitude)
        self.return_value=[self.temperature,self.bmp280.pressure,self.bmp280.altitude]
        return self.return_value
    def read_all(self):
        self.temperature = self.bmp280.temperature+self.temp_offset
        self.return_value=[self.temperature,self.bmp280.pressure,self.bmp280.altitude]
        return self.return_value
        
        

    def get_temperature(self):
        self.temperature = self.bmp280.temperature+self.temp_offset
        return self.temperature
    def get_pressure(self):
        self.pressure=self.bmp280.pressure
        return self.pressure
        
    def get_altitude(self):
        self.altitude=self.bmp280.altitude
        return self.altitude
