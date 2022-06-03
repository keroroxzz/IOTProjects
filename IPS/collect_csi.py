import sys
import time
import serial

#
# Append subsequent lines with the current timestamp
#
port = "/dev/ttyUSB0"
ser = serial.Serial(port, 921600)
count = 0

def close():
    ser.close()
    sys.exit(0)

if not ser.is_open:
    ser.open()

while ser.is_open and count < 50:
    try:
        line = ser.readline()
        line = line.decode('utf-8')
    except UnicodeDecodeError as e:
        continue
    except KeyboardInterrupt as e:
        close()

    if "CSI_DATA" in line:
        print(line.rstrip() + "," + str(time.time()))
        count += 1

close()
