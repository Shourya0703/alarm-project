
# Alarm Clock 


import datetime
import time
import pyttsx3

def speak(text):
    engine = pyttsx3.init()  # ← Re-initialize engine every time
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def simple_alarm_clock():
    print("--- Simple Python Alarm Clock (With pyttsx3 Sound) ---")

    try:
        alarm_hour = int(input("Set Hour (0-23): "))
        alarm_minute = int(input("Set Minute (0-59): "))
        alarm_message = input("Set Alarm Message: ")
    except ValueError:
        print("Invalid input. Please enter whole numbers for hour and minute.")
        return

    if not (0 <= alarm_hour <= 23 and 0 <= alarm_minute <= 59):
        print("Invalid time entered. Hour must be 0-23 and Minute 0-59.")
        return

    print(f"\n⏰ Alarm set for {alarm_hour:02d}:{alarm_minute:02d}. Waiting...")

    while True:
        now = datetime.datetime.now()
        current_hour = now.hour
        current_minute = now.minute

        if current_hour == alarm_hour and current_minute == alarm_minute:
            print("\n" * 4)
            print("************************************************")
            print("🚨 🚨 🚨 ALARM! 🚨 🚨 🚨")
            print(f"Time is {current_hour:02d}:{current_minute:02d}")
            print(f"MESSAGE: {alarm_message}")
            print("************************************************")

            # 🔊 Alarm repeating (10 times)
            for _ in range(10):
                speak("Alarm ringing! " + alarm_message)
                time.sleep(0.5)

            break

        time.sleep(1)

simple_alarm_clock()




# SYSTEM ARCHITECTURE
'''
+----------------------------------------+
|            User Input Layer            |
+----------------------------------------+
|  Input Validation & Error Handling     |
+----------------------------------------+
|   Real-Time System Clock Monitoring    |
+----------------------------------------+
|       Alarm Trigger & Voice Output     |
+----------------------------------------+
|     Operating System Time Services     |
+----------------------------------------+


'''

# WORKFLOW DIAGRAM

'''

Start
  |
Enter Hour, Minute, Message
  |
Validate Input?
  |--No--> Show Error → End
  |--Yes
  |
Start Monitoring Time (Loop)
  |
Match Alarm Time?
  |--No--> Wait 1 sec → Loop again
  |--Yes
  |
Speak Alarm Message Repeatedly
  |
End

'''


# Sequence Diagram
'''

User           System           pyttsx3
 |               |                 |
 |--Input------->|                 |
 |               |                 |
 |               |--Validate------>|
 |               |                 |
 |               |--Check Time---->|
 |               |                 |
 |               |--Trigger Alarm->|
 |               |--Speak()------->|-->Voice Output
 |               |--Speak()------->|-->Voice Output

 
'''

# Component Diagram

'''

+------------------------+
| simple_alarm_clock()   |
+------------------------+
| - Input handling       |
| - Time monitoring      |
| - Alarm trigger        |
+------------------------+

+------------------------+
| speak()                |
+------------------------+
| - pyttsx3 engine       |
| - Voice generation     |
+------------------------+

'''


