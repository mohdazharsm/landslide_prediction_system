from communicate import Communicate, get_value
from writeCsv import writeData, makeFile, writeTrainingData
from processData import processData
from neuton import send_request
from collections import Counter
import time
import keyboard
import csv

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


def predictNeuton():
    send_request(
        url="ADD_YOUR_URL_HERE",
        file_path="data.csv",
    )


def predict(file_name="result.csv"):
    with open(file_name, "r") as f:
        column = (row[0] for row in csv.reader(f))
        color = Counter(column).most_common(1)[0][0]
        print("Most frequent value: {0}".format(color))
        return color


def setGatewayColor(gateway, color="white"):
    if color == "white":
        gateway.white()
    elif color == "green":
        gateway.green()
    elif color == "yellow":
        gateway.blue()
    elif color == "orange":
        gateway.orange()
    elif color == "red":
        gateway.red()
    elif color == "magenta":
        gateway.magenta()
    else:
        gateway.white()


if connected:
    makeFile()
    makeFile(file_name="data.csv")
    valdiDataCount = 0  # count of valid data
    calDataCount = 20  # for calibration
    processedDataCount = 0
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

                    # Prediction
                    writeData(processedData, file_name="data.csv")
                    if processedDataCount == 5:
                        processedDataCount = 0
                        predictNeuton()
                        color = predict()
                        setGatewayColor(gateway, color)

                    try:
                        # for re-calibration (gyroscope data)
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
