import modules as mod
import datetime

#fill this dictionary with the various IDs and the corresponding student names.s
studentID = {
    "0036000291452": "Teon Morgan"
}

#starts up the webcam to stream video
vs = mod.initializeStream()
#opens the file for storage
csv = mod.openFile(str(datetime.datetime.now().date())+".csv")
#initializes the class to write to the csv file
writer = mod.initializeWrite(csv)
#calls the loop which handles the decoding of the video frames and the saving of data
mod.loop(vs, csv, writer, studentID)