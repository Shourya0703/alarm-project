
# Alarm Clock 


import datetime
import time
import pyttsx3
#Made a small function judt for speaking the alarm message
def speak(text):
    engine = pyttsx3.init()  # Had to re- init the engine every time because otherwise pyttxs3 only talks once
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def simple_alarm_clock():
    print("--- Simple Python Alarm Clock (With pyttsx3 Sound) ---")

    try:
        #Taking hour & minutes from user.
        #Sticking to 24 hr format so it's easy to compare
        alarm_hour = int(input("Set Hour (0-23): "))
        alarm_minute = int(input("Set Minute (0-59): "))
        #The message the alarm should speak
        alarm_message = input("Set Alarm Message: ")
    except ValueError:
        #If user types something other than numbers, this will catch it
        print("Invalid input. Please enter whole numbers for hour and minute.")
        return
    #Basic range check so user doesn't put something impossible
    if not (0 <= alarm_hour <= 23 and 0 <= alarm_minute <= 59):
        print("Invalid time entered. Hour must be 0-23 and Minute 0-59.")
        return

    print(f"\n⏰ Alarm set for {alarm_hour:02d}:{alarm_minute:02d}. Waiting...")

    #Program keeps checking the system time every second
    while True:
        now = datetime.datetime.now()
        current_hour = now.hour
        current_minute = now.minute

        #If the time matches the alarm, then we trigger it
        if current_hour == alarm_hour and current_minute == alarm_minute:
            print("\n" * 4)
            print("************************************************")
            print("🚨 🚨 🚨 ALARM! 🚨 🚨 🚨")
            print(f"Time is {current_hour:02d}:{current_minute:02d}")
            print(f"MESSAGE: {alarm_message}")
            print("************************************************")

            # Alarm repeating 10 times so the user doesn't miss it
            for _ in range(10):
                speak("Alarm ringing! " + alarm_message)
                time.sleep(0.5) #Small delay so it doesn't overlap sound

            break  #exit after alarm finishes

        time.sleep(1)  #just checking time once per second to save CPU

#Calling the main function
simple_alarm_clock()

#CODE END



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



