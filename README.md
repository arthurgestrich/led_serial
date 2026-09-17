# led_serial
Aplicação web desenvolvida com Flask e HTML para controlar um LED conectado a um Arduino através de comunicação serial.

Controle de LED com Flask e Arduino

Requisitos

Arduino

LED conectado à porta digital 2

Arduino conectado à porta serial COM3

Python

Flask

PySerial

*************************************************************
No código Python, a comunicação serial está configurada para:

arduino = serial.Serial('COM3', 9600)


Caso o Arduino esteja em outra porta, altere COM3 para essa porta.

O LED deve estar conectado à porta digital 2 do Arduino.
