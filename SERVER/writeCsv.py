import csv

fieldnames = [
    "Rain1",
    "Moisture1",
    "X1",
    "Y1",
    "Z1",
    "Rain2",
    "Moisture2",
    "X2",
    "Y2",
    "Z2",
]

fieldnamesForTrainignAI = [*fieldnames, "Target"]


def makeFile(file_name="incoming.csv", isTrainingData=False):
    with open(file_name, "w") as csv_file:
        csv_writer = csv.DictWriter(
            csv_file,
            fieldnames=fieldnamesForTrainignAI if isTrainingData else fieldnames,
        )
        csv_writer.writeheader()


def writeData(Input, file_name="incoming.csv"):
    with open(file_name, "a+", newline="") as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        try:
            info = {
                "Rain1": Input[0],
                "Moisture1": Input[1],
                "X1": Input[2],
                "Y1": Input[3],
                "Z1": Input[4],
                "Rain2": Input[5],
                "Moisture2": Input[6],
                "X2": Input[7],
                "Y2": Input[8],
                "Z2": Input[9],
            }
            csv_writer.writerow(info)
        except IndexError:
            print("No suficcient elemets")
        except TypeError:
            print("None type object cannot be saved")


def writeTrainingData(Input, Color, file_name="trainingData.csv"):
    with open(file_name, "a+", newline="") as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnamesForTrainignAI)
        infoWithTarget = {
            "Rain1": Input[0],
            "Moisture1": Input[1],
            "X1": Input[2],
            "Y1": Input[3],
            "Z1": Input[4],
            "Rain2": Input[5],
            "Moisture2": Input[6],
            "X2": Input[7],
            "Y2": Input[8],
            "Z2": Input[9],
            "Target": Color,
        }
        try:
            csv_writer.writerow(infoWithTarget)
        except IndexError:
            print("No suficcient elemets")
        except TypeError:
            print("None type object cannot be saved")
