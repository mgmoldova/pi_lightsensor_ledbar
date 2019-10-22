import grovepi
import time

# A0 = light sensor
# 0.1 - 40,000 LUX
light_sensor = 0

# D4 = servo
ledbar = 4

threshold = 10

grovepi.pinMode(light_sensor,"INPUT")
grovepi.pinMode(ledbar,"OUTPUT")

# main loop
if __name__ == '__main__':
    while True:
        try:
            sensor_value = grovepi.analogRead(light_sensor)

            resistance = (float)(1023 - sensor_value) * 10 / sensor_value

            for i in range(threshold):
                grovepi.ledBar_setLevel(ledbar, i)
                time.sleep(0.2)
            time.sleep(.3)
            
            print(f'Valoarea sensorului: {sensor_value}\nRezistenta: {resistance}')
            time.sleep(1)
        except IOError:
            print('Eroare!')
