# importing some shit that lets me have a timer 
# and that little messagebox that pops up!
import ctypes, time
from time import gmtime, strftime
# an infinite loop. usually a really bad practice, but 
# in this case it works whats it supposed to do which is
# repeating the action (notification) every n seconds
while True:
# a function "Water" which essentially creates the little pop up
    def Water(title, text, style):
        return ctypes.windll.user32.MessageBoxW(0, text, title, style)
# outputing current time to the console and showing me a pop up to remind
# me to drink some fucking water. cos im dumb as fuck and i laways forget
    print("notified at " + strftime("%H:%M", gmtime()))
    Water('hey!', 'drink some fucking water u never fucking drink enough of it!', 64)
# sleep for 3.6k seconds (an hour). basically means wait this amount of time
# until you show the message again
    time.sleep(3600)

