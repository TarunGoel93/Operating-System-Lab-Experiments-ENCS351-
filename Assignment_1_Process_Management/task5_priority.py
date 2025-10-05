import os, time

def cpu_task():
    for i in range(10000000):
        pass
    print(f"Process {os.getpid()} completed.")

def task5():
    for i in range(3):
        pid = os.fork()
        if pid == 0:
            os.nice(i * 5)
            print(f"Child PID={os.getpid()}, nice={i*5}")
            cpu_task()
            os._exit(0)
    for i in range(3):
        os.wait()
