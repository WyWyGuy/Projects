from microbit import *
steps=0

while True:
    if button_a.is_pressed():
        while True:
            if accelerometer.was_gesture('shake'):
                steps += 1
                display.show(steps)
    if button_b.is_pressed():
        while True:
            if accelerometer.was_gesture('shake'):
                steps += 1
            if button_a.is_pressed():
                display.scroll(steps)
    if accelerometer.was_gesture('shake'):
        while True:
            if accelerometer.get_y() > 1500:
                steps += 1
                display.scroll(steps, delay=100)