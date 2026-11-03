
import time
from datetime import datetime
import winsound

alarm_time = input("Enter alarm time (HH:MM:SS): ")

print("Alarm set for:", alarm_time)

while True:
    current_time = datetime.now().strftime("%H:%M:%S")

    if current_time == alarm_time:
        print("⏰ WAKE UP! ALARM!")
        
        for i in range(5):
            winsound.Beep(1000, 1000)
        
        break

    time.sleep(1)
