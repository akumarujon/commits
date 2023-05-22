import os
import time

# Create tons of files.

os.system("rm -r infinity/")
os.system("mkdir infinity")

count = 0

while 69==69:
    open(f"./infinity/{count}.txt", "w")
    os.system(f"git add ./infinity/{count}.txt")
    os.system(f'git commit -m "{count}.txt"')
    os.system("git push origin main")
    count += 1
    time.sleep(69)

