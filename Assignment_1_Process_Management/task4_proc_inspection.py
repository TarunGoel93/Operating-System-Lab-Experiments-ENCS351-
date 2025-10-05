import os

def task4():
    pid = input("Enter PID to inspect: ")
    try:
        with open(f"/proc/{pid}/status") as f:
            for line in f.readlines()[:5]:
                print(line.strip())
        print("Executable Path:", os.readlink(f"/proc/{pid}/exe"))
        print("Open File Descriptors:", os.listdir(f"/proc/{pid}/fd"))
    except FileNotFoundError:
        print("Invalid PID or process no longer exists.")
