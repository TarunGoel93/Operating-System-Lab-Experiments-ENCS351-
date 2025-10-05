import os

def task1():
    n = int(input("Enter number of child processes: "))
    for i in range(n):
        pid = os.fork()
        if pid == 0:
            print(f"Child {i+1}: PID={os.getpid()}, Parent PID={os.getppid()}")
            os._exit(0)
    for i in range(n):
        os.wait()
    print("All child processes finished.")
