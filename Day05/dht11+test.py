# 온습도 센서 DHT11
import Adafruit_DHT as dht
import time

sensor = dht.DHT11 # 초 저가 센서
rcv_pin = 17

try:
    while True:
        humid, temp = dht.read_retry(sensor, rcv_pin)
        if humid is not None and temp is not None:
            print(f'온도 : {temp}C  /  습도 : {humid}% ')
        else:
            print('센싱 에러')

        time.sleep(1)
except Exception as e:
    print(e)
finally:
    print('---프로그램 종료 ----')