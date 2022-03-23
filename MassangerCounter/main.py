import json
import os

import datetime


def getMassages():
    massages = []
    for files in os.listdir(os.getcwd()):
        if files.endswith("json") and files == "message_2.json":
            with open(files) as f:
                data = json.loads(f.read())
                massages += data["messages"]
    return massages


def countAllMassages(massages):
    count = 0
    count += len(massages)
    return count


def getMassagesPerDay(massages):
    day = 0
    personCounterList = []
    for x in range(len(massages)):
        timestamp = int(massages[x]["timestamp_ms"])
        your_dt = datetime.datetime.fromtimestamp(int(timestamp) / 1000)

        if your_dt.day != day:
            print(str(your_dt.day) + "  :  " + str(day))
            print(massages[x]["sender_name"])
            print(your_dt.strftime("%Y-%m-%d %H:%M:%S"))
            day = your_dt.day
            print("=" * 50)
            personCounterList.append(massages[x]["sender_name"])

    print(personCounterList)
    return personCounterList


def getMassagesPerSpecificAmoutOfHours(massages, hours):
    previousTime = 0
    personCounterList = []
    for x in range(len(massages)):
        timestamp = int(massages[x]["timestamp_ms"])
        your_dt = datetime.datetime.fromtimestamp(int(timestamp) / 1000)
        # print(your_dt.strftime("%Y-%m-%d %H:%M:%S"))
        # print(your_dt)
        # print(previousTime)
        if previousTime == 0:
            previousTime = your_dt
        difference = previousTime - your_dt
        if round(difference.total_seconds() / 3600) > hours:
            print(massages[x]["sender_name"])
            print(your_dt)
            print(previousTime)
            print(difference)
            print(round(difference.total_seconds() / 3600))
            print("=" * 50)
        previousTime = your_dt

    print(personCounterList)
    return personCounterList


def getMassagesWithWords(massages, words):
    foundedMassages = []
    pom = 0
    for x in range(len(massages)):
        if "content" in massages[x]:
            for word in words:
                if word in massages[x]["content"].lower():
                    print(massages[x]["content"] + "   " + massages[x]["sender_name"])
                    foundedMassages.append(massages[x]["sender_name"])
            pom += 1
    print(pom)
    return foundedMassages


def printingResults(list):
    print('\n\n\n')
    print("=" * 50)
    print("Adam Wieczarek: " + str(list.count("Adam Wieczarek")))
    print("Monika Szumska: " + str(list.count("Monika Szumska")))
    print("=" * 50)


if __name__ == '__main__':
    massages = getMassages()
    print(countAllMassages(massages))

    # list = getMassagesWithWords(massages, ["hejka", "Hejka", "hej", "Hej", "ej", "Ej"])
    # printingResults(list)

    # list = getMassagesWithWords(massages, ["lecimy", "idziemy"])
    # printingResults(list)

    massagesPerDay = getMassagesPerDay(massages)
    printingResults(massagesPerDay)

    # list = getMassagesPerSpecificAmoutOfHours(massages, 5)
    # printingResults(list)
