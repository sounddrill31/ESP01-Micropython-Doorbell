from machine import Pin
import urequests

import network

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect("<SSID>", "<PASSWORD>")

while not sta_if.isconnected():
    pass

print("Connected to Wi-Fi")

button = Pin(0, Pin.IN, Pin.PULL_UP)
led = Pin(2, Pin.OUT)

while True:
    if not button.value():
        led.value(1) #invert this as you want, my esp01S turns led on when asked to turn off and vice versa 
        url = "https://maker.ifttt.com/trigger/{event}/with/key/{your_key}"
        response = urequests.post(url)
        response.close()
    else:
        led.value(0) #invert this as you want, my esp01S turns led on when asked to turn off and vice versa 
