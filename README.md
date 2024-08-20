# Keylogger
Simple Keylogger

This is used to monitor and record each key stroke of your keyboard and store it to a text file called "<your_device_name>_KEYLOG.txt".

Note: It cannot identify or understand complex commands combo such as: CTRL+C, SHIFT+(special symbol), CTRL+ALT+DEL, etc.

**Warning/Disclaimer: This is strictly for educational and ethical purposes. Any form of misuse of this program for any particular reason shall be considered as a crime and will be a punishable offence. It is advised to use it on your own personal device in a virtual environment. If this program is to be used for/on/by someone else, then consent/permission of the owner of the targetted deivce is mandatory. The owner of this script is not responsible for any misuse by anyone.** 

Pre-requiremnts:
- Python 3.9 or higher
- Virtual environment/sandbox (preferred)
- Libraries -> socket, pynput, datetime

How to use:

1) Make the required changes to the "die" variable and set to a time in the future
2) Run the script
3) Type in anything alphabets, numbers, special keys etc.
4) Wait till the script terminates
5) Use the file name to navigate to the file in your system (by default the log file gets saved on -> "C:/Users/<user>")
6) Open the keylog file to view what has been captured

How to set file path of logfile:

- Go to the destination folder/location where you want your logfile to be saved
- Copy the path of that location and paste it before "{0}" in every open() function
- After pasting, replace each "\" (backslash) with a "/" (forward slash)
- Save the script file and continue with the above steps to use

How to set "die" variable value:

timedelta() is used to modify the current time to something else in the future or the past. Some of its parameters are -> hours, minutes, seconds

*You can use these parameters individually or together to set the end time. 

Example: ....timedelta(hours=1)
         ....timedelta(minutes=18)
         ....timedelta(seconds=22)
         
**Remember not to set the time to the past as it may lead to immediate termination of the script.

For further reference and understanding, visit https://www.geeksforgeeks.org/python-datetime-timedelta-function/
