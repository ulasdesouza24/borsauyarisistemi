from forex_python.converter import CurrencyRates
from playsound import playsound
import time

c = CurrencyRates()
mem = c.get_rate('USD' , 'TRY')

while True:
    kur = c.get_rate('USD' , 'TRY')
    print(kur)

    if kur>mem:
            print("artti")
            playsound("ses.mp3")
            mem = kur

    time.sleep(5)
