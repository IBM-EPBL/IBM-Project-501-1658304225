import pywhatkit
import random
from datetime import datetime
n = 10
while n > 0:
    date_time = str(datetime.now())
    t = random.randint(30, 45)
    print("Temperature:",t)
    h = random.randint(30, 75)
    print("Humidity:",h)
    if t > 36:
        pywhatkit.sendwhatmsg("+918220308951", "HIGH TEMP DETECTED", int(date_time[11:13]), int(date_time[14:16]) + 1)

    n = n - 1




