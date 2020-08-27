import json
import os.path

def loadFile(filename):
    with open(filename, "r") as load:
        data = json.load(load)
    return data

def saveFile(filename, studentID):
    with open(filename, "w") as save:
        json.dump(studentID, save)

def writeToFile(studentID):
    number = input("Enter Student ID: ")
    if number in studentID:
        print("This ID is present, the entered name will overwrite the ID value.")
    name = input("Enter Student Name: ")
    studentID[number] = name
    return studentID

def deleteEntry(delete, idList):
    if delete in idList:
        idList.pop(delete)
        return idList
    else:
        print("This ID is not in the file.")
        return idList

def removeFromFile(path):
    if os.path.isfile(path):
        idList = loadFile(path)
        print("Enter an ID to delete it.")
        print("Enter Ctrl + C when finished entering.")
        while True:
            try:
                print("Available IDs = "+str(idList.keys()))
                print("Corresponding Names = "+str(idList.values()))
                toDelete = input("ID: ")
                idList = deleteEntry(toDelete, idList)
            except KeyboardInterrupt:
                saveFile(path, idList)
                exit(0)

    else:
        print("No file to delete from.")
        exit(0)


def addToFile(path):
    if os.path.isfile(path):
        idList = loadFile(path)
    else:
        idList = {}
    print("Enter Ctrl + C when finished entering.")
    while True:
        try:
            idList = writeToFile(idList)
        except KeyboardInterrupt:
            saveFile("Student-ID.json", idList)
            exit(0)
    
