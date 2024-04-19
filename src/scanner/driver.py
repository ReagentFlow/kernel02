import serial
from src.constants import SCANNER_PORT


def barcode_scanner():
    ser = serial.Serial(SCANNER_PORT, 9600, timeout=1)
    s = ser.readline()
    while s == b'':
        s = ser.readline()
    ser.close()
    return s


if __name__ == '__main__':
    for _ in range(20):
        print(barcode_scanner())
