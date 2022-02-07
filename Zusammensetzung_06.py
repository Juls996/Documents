import os
import time
import sys
import shutil

patha = "C:\\Users\\taskin\\Downloads\\Test01_release\\"
phatb = "C:\\Users\\taskin\\Documents\\Test01\\"


def look_for_folder_in_patches():
    patch_folder = "C:\\Users\\taskin\\Documents\\Test01\\NEU\\"
    install_folder = "C:\\Users\\taskin\\Documents\\Test01\\FERTIG\\"
    filename = "viewer.txt"
    new_version = "5.5.5"
#start
    # Patch-mtime auslesen
    full_patch_path = patch_folder + new_version + "\\"
    patch_mtime = os.path.getmtime(full_patch_path + filename)

    # Falls Ordner noch nicht im install-Verzeichnis vorhanden : erstellen
    if not os.path.exists(install_folder + new_version):
        os.mkdir(install_folder + new_version)
#end
    # vorherige Patchversion finden
    previous_version = new_version.split(".")
    previous_version[2] = str(int(previous_version[2]) - 1)
    previous_version = ".".join(previous_version)

    # und mtime auslesen
    previous_patch_mtime = os.path.getmtime(install_folder + previous_version + "\\" + filename)

    # variable setzen, die angibt, ob die mtime der patchdatei größer ist (die datei ist also jünger (neu erstellt))
    patch_is_new = previous_patch_mtime < patch_mtime

    if patch_is_new:
        print(shutil.copy(full_patch_path + filename, install_folder + new_version + "\\"))


look_for_folder_in_patches()



"""

files = os.listdir(patha)
files.sort()
for x in files:
    A = patha + x
    B = phatb + x
    shutil.move(A, B)

path = "C:\\Users\\taskin\\Documents\\Test01"
destination = "C:\\Users\\taskin\\Documents\\Test01\\Backup\\jx_" + time.strftime('%d.%m.%Y') + '_' + time.strftime('%H.%M.%S'  ) + ".txt"


jx = os.path.getmtime(destination)
jxA = time.strftime('%d.%m.%Y %H:%M')


def TimeStampCheck():
    jx = os.path.getmtime(destination)
    timedif = time.time() - jx
    if timedif > 24*60*60:
        print("Keine neue Version vorhanden.")
        sys.exit()
    else:
        shutil.copy(path, destination)
        print("Datei gesichert.")

TimeStampCheck()
"""
