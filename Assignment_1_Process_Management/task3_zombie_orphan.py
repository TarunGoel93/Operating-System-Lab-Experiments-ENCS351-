import os, time

def task3():
    print("\n--- ZOMBIE PROCESS DEMO ---")
    pid = os.fork()
    if pid == 0:
        print("Child (Zombie demo) exiting...")
        os._exit(0)
    else:
        time.sleep(5)
        print("Check using: ps -el | grep defunct")
        os.wait()

    print("\n--- ORPHAN PROCESS DEMO ---")
    pid = os.fork()
    if pid > 0:
        print("Parent exiting before child...")
        os._exit(0)
    else:
        time.sleep(5)
        print(f"Child became orphan. New Parent PID: {os.getppid()}")
