from writeCsv import writeData, makeFile
import pandas as pd


def processData(count, calCount):
    try:
        data = pd.read_csv("incoming.csv")
        # x = data.index.values
        Rain1 = getRainOrMositureAvg(data, count, "Rain1")
        Moisture1 = getRainOrMositureAvg(data, count, "Moisture1")
        X1 = getGyroscopeAvg(data, calCount, count, "X1")
        Y1 = getGyroscopeAvg(data, calCount, count, "Y1")
        Z1 = getGyroscopeAvg(data, calCount, count, "Z1")
        Rain2 = getRainOrMositureAvg(data, count, "Rain2")
        Moisture2 = getRainOrMositureAvg(data, count, "Moisture2")
        X2 = getGyroscopeAvg(data, calCount, count, "X2")
        Y2 = getGyroscopeAvg(data, calCount, count, "Y2")
        Z2 = getGyroscopeAvg(data, calCount, count, "Z2")
        writeData(
            [Rain1, Moisture1, X1, Y1, Z1, Rain2, Moisture2, X2, Y2, Z2],
            "processedData.csv",
        )
        return [Rain1, Moisture1, X1, Y1, Z1, Rain2, Moisture2, X2, Y2, Z2]
    except:
        pass


def getGyroscopeAvg(
    data,
    count,
    calCount,
    name,
):
    return abs(
        data[calCount - 20 : calCount][name].mean()
        - data[count - 5 : count][name].mean()
    )


def getRainOrMositureAvg(data, count, name):
    return abs(data[count - 20 : count][name].mean())
