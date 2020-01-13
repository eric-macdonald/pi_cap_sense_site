from flask import Flask, render_template
import subprocess
import os
import touchphat
import datetime
import time
app = Flask(__name__)

def enter():
    touchphat.all_on()
    return

def back():
    touchphat.all_off()
    return

tempString = "Youngstown State University Capacitive Sensor\n"
ledsSTATE = False 

@touchphat.on_touch(['Back','A','B','C','D','Enter'])
def handle_touch(event):
    global tempString
    now = datetime.datetime.now()
    timeString = now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    tempString = tempString + str(event.channel) + " " + timeString + "\n"
    return


@app.route("/")
def check():
    global tempString
    global ledsSTATE
    if(ledsSTATE):
        ledsSTATE = False
        touchphat.all_off()
    else:
        ledsSTATE = True
        touchphat.all_on()
    return  "<xmp>" + tempString  + "</xmp>"


if __name__ == "__main__":
    #for pad in ['Back','A','B','C','D','Enter']:
    #    touchphat.set_led(pad, True)
    #    time.sleep(0.1)
    #    touchphat.set_led(pad, False)
    #    time.sleep(0.1)
    app.run(host='0.0.0.0', port=5000, debug=True)
    #signal.pause()
