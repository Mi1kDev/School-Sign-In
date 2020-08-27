import scannerModule as mod
import datetime
import persistenceModule as persist
import os.path

#fill this dictionary with the various IDs and the corresponding student names.
if os.path.isfile("Student-ID.json"):
    studentID = persist.loadFile("Student-ID.json")
else:
    print("Please create the Student-ID.json file by running the addAndRemove file.")
    exit(0)
#starts up the webcam to stream video
vs = mod.initializeStream()
#opens the file for storage
csv = mod.openFile(str(datetime.datetime.now().date())+".csv")
#initializes the class to write to the csv file
writer = mod.initializeWrite(csv)
#calls the loop which handles the decoding of the video frames and the saving of data
mod.loop(vs, csv, writer, studentID)