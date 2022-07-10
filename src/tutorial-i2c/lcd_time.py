from RPLCD.i2c import CharLCD
import time

lcd = CharLCD(i2c_expander="PCF8574", address=0x27)
lcd.write_string("Raspberry Pi")

try:
    while True:
        lcd.cursor_pos = (1, 0)
        lcd.write_string(time.strftime("%H:%M:%S"))
        time.sleep(1)

finally:
    lcd.close(True)

