import smbus
import time
import RPi.GPIO as GPIO

#KEYPAD SETUP
L1 = 4
L2 = 17
L3 = 26
L4 = 22

C1 = 5
C2 = 6
C3 = 13
C4 = 19

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(L1, GPIO.OUT)
GPIO.setup(L2, GPIO.OUT)
GPIO.setup(L3, GPIO.OUT)
GPIO.setup(L4, GPIO.OUT)

GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def readLine(line, characters):
    GPIO.output(line, GPIO.HIGH)
    if(GPIO.input(C1) == 1):
        register(characters[0])
        while GPIO.input(C1) == 1:
            pass
    if(GPIO.input(C2) == 1):
        register(characters[1])
        while GPIO.input(C2) == 1:
            pass
    if(GPIO.input(C3) == 1):
        register(characters[2])
        while GPIO.input(C3) == 1:
            pass
    if(GPIO.input(C4) == 1):
        register(characters[3])
        while GPIO.input(C4) == 1:
            pass
    GPIO.output(line, GPIO.LOW)



#LCD SCREEN SETUP
I2C_ADDR  = 0x27 # I2C device address
LCD_WIDTH = 16   # Maximum characters per line
LCD_CHR = 1 # Mode - Sending data
LCD_CMD = 0 # Mode - Sending command
line1 = 0x80 # LCD RAM address for the 1st line
line2 = 0xC0 # LCD RAM address for the 2nd line
LCD_BACKLIGHT  = 0x08  # On
ENABLE = 0b00000100 # Enable bit
E_PULSE = 0.0005
E_DELAY = 0.0005
bus = smbus.SMBus(1) # Rev 2 Pi uses 1

def lcd_init():
  lcd_byte(0x33,LCD_CMD) # 110011 Initialise
  lcd_byte(0x32,LCD_CMD) # 110010 Initialise
  lcd_byte(0x06,LCD_CMD) # 000110 Cursor move direction
  lcd_byte(0x0C,LCD_CMD) # 001100 Display On,Cursor Off, Blink Off 
  lcd_byte(0x28,LCD_CMD) # 101000 Data length, number of lines, font size
  lcd_byte(0x01,LCD_CMD) # 000001 Clear display
  time.sleep(E_DELAY)
  
def lcd_byte(bits, mode):
  bits_high = mode | (bits & 0xF0) | LCD_BACKLIGHT
  bits_low = mode | ((bits<<4) & 0xF0) | LCD_BACKLIGHT
  bus.write_byte(I2C_ADDR, bits_high)
  lcd_toggle_enable(bits_high)
  bus.write_byte(I2C_ADDR, bits_low)
  lcd_toggle_enable(bits_low)
  
def lcd_toggle_enable(bits):
  time.sleep(E_DELAY)
  bus.write_byte(I2C_ADDR, (bits | ENABLE))
  time.sleep(E_PULSE)
  bus.write_byte(I2C_ADDR,(bits & ~ENABLE))
  time.sleep(E_DELAY)
  
def display(message,line):
  message = message.ljust(LCD_WIDTH," ")
  lcd_byte(line, LCD_CMD)
  for i in range(LCD_WIDTH):
    lcd_byte(ord(message[i]),LCD_CHR)

def clear():
    display("",line1)
    display("",line2)



#MY CODE

enter = ""
coded = ""
key = "1234"

def main():
  while True:
    detect()

def detect():
    readLine(L1, ["1","2","3","A"])
    readLine(L2, ["4","5","6","B"])
    readLine(L3, ["7","8","9","C"])
    readLine(L4, ["*","0","#","D"])
    time.sleep(0.05)

def register(character):
    global enter
    global coded
    global key
    
    if len(enter) == 4 and character == "#":
        if enter == key:
            display("ACCESS GRANTED", line1)
            display("Please Enter", line2)
            enter = ""
            coded = ""
            time.sleep(3)
            clear()
        else:
            display("INCORRECT CODE", line1)
            display("ACCESS DENIED", line2)
            enter = ""
            coded = ""
    elif len(enter) < 4:
        if character != "*" and character != "#" and character != "A" and character != "B" and character != "C" and character != "D":
            enter += character
            coded += "*"
            display(coded, line1)
            display("", line2)
    else:
        display("Invalid Input", line2)
        display(coded, line1)
        enter = ""
        coded = ""



try:
    lcd_init()
    display("Enter Passcode", line1)
    display("Press # to Enter", line2)
    main()
except KeyboardInterrupt:
    clear()
finally:
    clear()
