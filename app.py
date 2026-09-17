from flask import Flask, render_template
import serial
import time

app = Flask(__name__)

arduino = serial.Serial('COM3', 9600)
time.sleep(2)  

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ligar')
def ligar():
    arduino.write(b'1')
    return "LED ligado"

@app.route('/desligar')
def desligar():
    arduino.write(b'0')
    return "LED desligado"

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)