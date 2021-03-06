from communicate import Communicate, get_value
from writeCsv import writeData, makeFile, writeTrainingData
from processData import processData
import time
import keyboard

port = "COM11"
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


# color for training data
Color = "white"

if connected:
    makeFile()
    makeFile(file_name="trainingData.csv")
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
                    # setting color and storing training data
                    writeTrainingData(processedData, Color)
                    try:
                        # for re-calibration (gyroscope data)
                        if keyboard.is_pressed("c"):
                            print("Re-Callibrating...")
                            calDataCount = valdiDataCount - 1
                        elif keyboard.is_pressed("w"):
                            Color = "white"
                        elif keyboard.is_pressed("g"):
                            Color = "green"
                        elif keyboard.is_pressed("y"):
                            Color = "yellow"
                        elif keyboard.is_pressed("o"):
                            Color = "orange"
                        elif keyboard.is_pressed("r"):
                            Color = "red"
                        elif keyboard.is_pressed("m"):
                            Color = "magenta"
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
