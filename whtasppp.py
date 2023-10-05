import pywhatkit as w
import time
import pyautogui
import keyboard as k

# Phone number or contact name of the recipient
recipient = "+393295363368"  # Replace with the recipient's number

message = "Hello, does I deserve a blowjob?"

names = [
    "Cristiano Ronaldo",
    "Paulo Dybala",
    "Giorgio Chiellini",
    "Leonardo Bonucci",
    "Wojciech Szczęsny",
    "Federico Chiesa",
    "Dejan Kulusevski",
    "Weston McKennie",
    "Juan Cuadrado",
    "Matthijs de Ligt",
    "Aaron Ramsey",
    "Arthur Melo",
    "Adrien Rabiot",
    "Danilo",
    "Alex Sandro"
]

# Format the names into a string with each name on a separate line
formatted_names = "\n".join(names)

# Specify the time in 24-hour format (hour and minute)
hour = 23  # Replace with the desired hour
minute = 40  # Replace with the desired minute

# Set the wait_time in seconds (e.g., 20 seconds)
wait_time = 10

# Calculate the call_time
call_hour = hour
call_minute = minute + wait_time // 60
call_time = (call_hour, call_minute)

# Send the message
w.sendwhatmsg(recipient, message, call_time[0], call_time[1])
#w.sendwhatmsg(recipient, formatted_names, call_time[0], call_time[1])
pyautogui.click(1050, 950)
time.sleep(2)
k.press_and_release('enter')






