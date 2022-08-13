import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number  = "0123456789"
symbol = ".,-#+*'_:;!$"

all = lower + upper + number + symbol
lenght = 11
password = "".join(random.sample(all, lenght))
print("Your password:",password)