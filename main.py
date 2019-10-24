import grovepi
import time

# A0 = light sensor
# 0.1 - 40,000 LUX
light_sensor = 0

# D4 = servo
ledbar = 4

# D10 = potentiomentr
threshold = 10

# Setup pins
grovepi.pinMode(light_sensor,"INPUT")
grovepi.pinMode(ledbar,"OUTPUT")


def normalize(x, in_min, in_max, out_min, out_max):
    '''Normalize a number from one range to another.'''
    return int((x-in_min) * (out_max-out_min) / (in_max-in_min) + out_min)

# main loop
if __name__ == '__main__':
    while True:
        try:
            sensor_value = grovepi.analogRead(light_sensor)
            resistance = normalize(sensor_value, 0, 1023, 0, 10)
            if resistance < threshold:
                grovepi.ledBar_setLevel(ledbar, int(resistance))
                time.sleep(0.2)
            else:
                grovepi.ledBar_setLevel(ledbar, 10)
            
            print(f'Valoarea sensorului: {sensor_value}\nRezistenta: {resistance}')
            time.sleep(1)
        except IOError:
            print('Eroare!')
