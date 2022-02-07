import os
import time
import sys
import shutil
path = r"C:\\Users\\taskin\\Documents\\Test01\\jx.txt"
destination = r"C:\\Users\\taskin\\Documents\\Test01\\Backup\\jx_" + time.strftime('%d.%m.%Y') + '_' + time.strftime('%H.%M.%S') + ".txt"

jx = os.path.getmtime(path)
jxA = time.strftime('%d.%m.%Y %H:%M')


def TimeStampCheck():
    jx = os.path.getmtime(path)
    timedif = time.time() - jx
    if timedif > 24*60*60:
        print("Keine neue Version vorhanden.")
        sys.exit()
    else:
        shutil.copy(path, destination)
        print("Datei gesichert.")

TimeStampCheck()


