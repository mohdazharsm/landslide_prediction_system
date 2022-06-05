from communicate import Communicate, get_value
from writeCsv import writeData, makeFile
from processData import processData
import time
import keyboard

port = "COM12"
connected = False
gateway = Communicate(port, 9600)
time.sleep(1)

if gateway.handshake():
    connected = True
    print("Connected")
else:
    print(" Not Connected")


def isValidData(Input):
    try:
        if (
            Input[0] == 0
            and Input[1] == 0
            and Input[2] == 0
            and Input[3] == 0
            and Input[4] == 0
            and Input[5] == 0
            and Input[6] == 0
            and Input[7] == 0
            and Input[8] == 0
            and Input[9] == 0
        ):
            print("No nodes connected")
            return False
        elif (
            Input[0] == 0
            and Input[1] == 0
            and Input[2] == 0
            and Input[3] == 0
            and Input[4] == 0
        ):
            print("First node not connected")
            return False
        elif (
            Input[5] == 0
            and Input[6] == 0
            and Input[7] == 0
            and Input[8] == 0
            and Input[9] == 0
        ):
            print("Second node not connected")
            return False
        else:
            return True
    except IndexError:
        return False


def conditionAlert(data):
    magenta = 35
    red = 10
    Rain1, Moisture1, X1, Y1, Z1, Rain2, Moisture2, X2, Y2, Z2 = data
    if (
        X1 > magenta
        or Y1 > magenta
        or Z1 > magenta
        or X2 > magenta
        or Y2 > magenta
        or Z2 > magenta
    ):
        gateway.magenta()
        print("Magenta")
    elif X1 > red or Y1 > red or Z1 > red or X2 > red or Y2 > red or Z2 > red:
        gateway.red()
        print("Red")
    elif (Rain1 > 100 or Moisture1 > 100) or (Rain2 > 100 or Moisture2 > 100):
        gateway.orange()
        print("Orange")
    elif (Rain1 > 60 or Moisture1 > 50) or (Rain2 > 60 or Moisture2 > 50):
        gateway.yellow()
        print("Yellow")
    elif (Rain1 > 20 or Moisture1 > 20) or (Rain2 > 20 or Moisture2 > 20):
        gateway.green()
        print("Green")
    else:
        gateway.white()
        print("White")


if connected:
    makeFile()
    valdiDataCount = 0  # count of valid data
    calDataCount = 20  # for calibration
    while True:
        try:
            Input = get_value(gateway)
            # print(valdiDataCount)
            if isValidData(Input):
                writeData(Input)
                valdiDataCount += 1
                if valdiDataCount == 20:
                    makeFile("processedData.csv")
                    pass
                if valdiDataCount > 25:
                    processedData = processData(valdiDataCount - 1, calDataCount)
                    print(processedData)
                    conditionAlert(processedData)
                    # for re-calibration (gyroscope data)
                    try:
                        if keyboard.is_pressed("c"):
                            print("Re-Callibrating...")
                            calDataCount = valdiDataCount - 1
                    except:
                        pass
                else:
                    gateway.loading()
                    print("Callibrating...")

            time.sleep(0.2)
        except IndexError:
            print("No suficcient elemets")
        except KeyboardInterrupt:
            gateway.close()
            break
        except:
            print("Error")
            break
