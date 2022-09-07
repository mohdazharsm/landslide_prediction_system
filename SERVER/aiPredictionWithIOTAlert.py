from communicate import Communicate, get_value
from writeCsv import writeData, makeFile
from processData import processData, isValidData
from onnxRun import predict
import time
import keyboard

port = "COM5"
nodeMCUport = "COM6"
connected = False
gateway = Communicate(port, 9600)
nodeMCU = Communicate(nodeMCUport, 9600)
time.sleep(1)

if gateway.handshake():
    connected = True
    print("Connected to gateway")
else:
    print("Not Connected gateway")

if nodeMCU.handshake():
    connected = True
    print("Connected to NodeMCU")
else:
    connected = False
    print("Not Connected to NodeMCU")


def predictColor(processedData):
    # colros in the order of the index of ml model (can be obtained by running the model using training data)
    colors = ["green", "magenta", "orange", "red", "white", "yellow"]
    index = predict(processedData)
    return colors[index]


def setGatewayColor(color="white"):
    if color == "white":
        gateway.white()
        nodeMCU.white()
    elif color == "green":
        gateway.green()
        nodeMCU.green()
    elif color == "yellow":
        gateway.yellow()
        nodeMCU.yellow()
    elif color == "orange":
        gateway.orange()
        nodeMCU.orange()
    elif color == "red":
        gateway.red()
        nodeMCU.red()
    elif color == "magenta":
        gateway.magenta()
        nodeMCU.magenta()
    else:
        gateway.white()
        nodeMCU.white()


if connected:
    makeFile()
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
                    # print(processedData)
                    # Prediction
                    color = predictColor(processedData)
                    # Alerting
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
