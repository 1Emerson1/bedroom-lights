import RPi.GPIO as GPIO
from flask import Flask, render_template, request

app = Flask(__name__)

RELAY_PIN = 26
isOn = False
    
#GPIO.setmode(GPIO.BCM)

@app.route('/')
def index():
    if (isOn):
        template_data = {
            'on': 'active',
            'off': 'default'
        }
    else:
        template_data = {
            'off': 'active',
            'on': 'default'
        }
    
    return render_template('main.html', **template_data)

@app.route("/on")
def turnOn():
    global isOn 
    isOn = True

    #GPIO.output(26, GPIO.LOW)
    template_data = {
            'on': 'active',
            'off': 'default'
    }
    
    return render_template('main.html', **template_data)

@app.route("/off")
def turnOff():
    global isOn 
    isOn = False

    GPIO.cleanup(RELAY_PIN)
    template_data = {
            'off': 'active',
            'on': 'default'
    }

    return render_template('main.html', **template_data)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)