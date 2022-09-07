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


# color for training data
Color = "white"

if connected:
    makeFile()
    makeFile(file_name="trainingData.csv", isTrainingData=True)
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
                    print(valdiDataCount - 25, Color)
                    print(processedData, "\n\n")
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
