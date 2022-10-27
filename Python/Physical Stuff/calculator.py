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
        calculate(characters[0])
        while GPIO.input(C1) == 1:
            pass
    if(GPIO.input(C2) == 1):
        calculate(characters[1])
        while GPIO.input(C2) == 1:
            pass
    if(GPIO.input(C3) == 1):
        calculate(characters[2])
        while GPIO.input(C3) == 1:
            pass
    if(GPIO.input(C4) == 1):
        calculate(characters[3])
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
    
def main():
  while True:
    detect()



#MY CODE
def detect():
    readLine(L1, ["1","2","3","A"])
    readLine(L2, ["4","5","6","B"])
    readLine(L3, ["7","8","9","C"])
    readLine(L4, ["*","0","#","D"])
    time.sleep(0.05)

problem = ""
answer = ""

def calculate(typed):
    global problem
    if str(typed) == "A":
        typed = "+"
    if str(typed) == "B":
        typed = "-"
    if str(typed) == "C":
        typed = "x"
    if str(typed) == "D":
        typed = "/"
    if str(typed) == "*":
        problem = problem[:-1]
        display(problem, line1)
    if str(typed) == "#":
        while GPIO.input(C3) == 1:
            pass
        solve()
    if typed != "*" and typed != "#":
        problem += str(typed)
        display(problem, line1)

def solve():
    global problem
    global answer
    
    problem = problem.replace('x','*')
    try:
        answer = str(eval(problem))
    except:
        answer = "Syntax Error"
    
    display(answer, line2)
    problem = ""
    answer = ""
    while True:
        detect()
        if problem != "":
            break
    display(problem, line1)
    main()



try:
    lcd_init()
    display("A=+ B=-  C=* D=/",line1)
    display("*=Delete #=Enter",line2)
    main()
except KeyboardInterrupt:
    clear()
finally:
    clear()