import datetime
import imutils
import time
import cv2
import csv as comma
import os.path
from pyzbar import pyzbar
from imutils.video import VideoStream

def initializeStream():
    vs = VideoStream(src=0).start()
    return vs

def openFile(path):
    if not os.path.isfile(path):
        csv = open(path, "w")
    else:
        csv = open(path, "a")
    return csv

def initializeWrite(csv):
    studentWriter = comma.writer(csv, delimiter=",")
    if csv.mode != "a":
        studentWriter.writerow(["Name", "Time of Scan"])
    return studentWriter

def writeRow(writer, string):
    writer.writerow([string, str(datetime.datetime.now().time())])


def loop(vs, csv, studentWriter, dictionary):
    found = set()
    times = []

    while True:
        frame = vs.read()

        barcodes = pyzbar.decode(frame)

        for barcode in barcodes:
            (x, y, w, h) = barcode.rect
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            barcodeData = barcode.data.decode("utf-8")
            barcodeType = barcode.type

            text = "{} ({})".format(barcodeData, barcodeType)
            cv2.putText(frame, text, (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
            if barcodeData not in found:
                if barcodeData in dictionary:
                    found.add(barcodeData)
                    times.append(str(datetime.datetime.now().time()))
                    print(times)
        
        cv2.imshow("Barcode Scanner", frame)
        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):
            break

    found = list(found)
    x = 0
    print(found)
    print(times)
    for i in found:
        if i in dictionary:
            print(i)
            studentWriter.writerow([dictionary[i], times[x]])
        x += 1
    studentWriter.writerow(["Finished Scanning @:" +str(datetime.datetime.now().time())])
    csv.close()
    cv2.destroyAllWindows()
    vs.stop()
