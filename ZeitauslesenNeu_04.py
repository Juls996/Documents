import os
import time

path = r"C:\\Users\\taskin\\Documents\\Test01\\jx.txt"

jx = os.path.getmtime(path)
jxA = time.strftime('%d.%m.%Y %H:%M')


print("Datei vom", jxA)

