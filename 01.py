import shutil
import os

patha = "C:/Users/taskin/Downloads/Test01_release/"
phatb = "C:/Users/taskin/Documents/Test01/"

files = os.listdir(patha)
files.sort()
for x in files:
    A = patha + x
    B = phatb + x
    shutil.move(A, B)

