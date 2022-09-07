from communicate import Communicate, get_value
from writeCsv import writeData, makeFile, writeTrainingData
from processData import processData, isValidData
import time
import keyboard

port = "COM5"
connected = False
gateway = Communicate(port, 9600)
time.sleep(1)

if gateway.handshake():
    connected = True
    print("Connected")
else:
    print(" Not Connected")


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
        return "magenta"
    elif X1 > red or Y1 > red or Z1 > red or X2 > red or Y2 > red or Z2 > red:
        gateway.red()
        print("Red")
        return "red"
    elif (Rain1 > 200 or Moisture1 > 31) or (Rain2 > 200 or Moisture2 > 31):
        gateway.orange()
        print("Orange")
        return "orange"
    elif (Rain1 > 100 or Moisture1 > 20) or (Rain2 > 100 or Moisture2 > 20):
        gateway.yellow()
        print("Yellow")
        return "yellow"
    elif (Rain1 > 30 or Moisture1 > 16) or (Rain2 > 30 or Moisture2 > 17):
        gateway.green()
        print("Green")
        return "green"
    else:
        gateway.white()
        print("White")
        return "white"


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
                    Color = conditionAlert(processedData)
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
