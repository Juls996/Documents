import os
import shutil
import sys
import time


pyt_path = "C:\\Users\\taskin\\Documents\\Test01"
sys.path.append(pyt_path)

files = list(map(lambda x: f"{pyt_path}\\{x}", next(os.walk(pyt_path), (None, None, []))[2]))

def getYYMMDD(filepath):
    statbuf = os.stat(filepath)
    date = time.localtime((statbuf.st_mtime))

    year = date[0]
    month = date[1]
    day = date[2]
    hour = date[3]
    minute = date[4]
    second = date[5]

    strYear = str(year)[2:]

    if (month <=9):
        strMonth = '0' + str(month)
    else:
        strMonth = str(month)

    if (day <=9):
        strDay = '0' + str(day)
    else:
        strDay = str(day)

    if (hour <=9):
        strHour = '0' + str(hour)
    else:
        strHour = str(hour)

    if (minute <=9):
        strMinute = '0' + str(minute)
    else:
        strMinute = str(minute)

    if (second <=9):
        strSecond = '0' + str(second)
    else:
        strSecond = str(second)
    return ('_' + strYear + strMonth + strDay + '_' + strHour + strMinute + strSecond)

newlist = []
for x in files:
    newlist.append(getYYMMDD(x))
out = newlist



fileName = "C:\\Users\\taskin\\Documents\\Test01\\jx.txt"
os.path.exists(fileName)
Out: True
fileName = "C:\\Users\\taskin\\Documents\\Test01"
os.path.exists(fileName)
out: True

print(fileName, "Datei Existiert bereits!")



patha = "C:/Users/taskin/Downloads/Test01_release/"
phatb = "C:/Users/taskin/Documents/Test01/"
files = os.listdir(patha)
files.sort()
for x in files:
    A = patha + x
    B = phatb + x
    shutil.move(A, B)
