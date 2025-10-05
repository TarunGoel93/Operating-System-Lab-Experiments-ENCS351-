import os

def task2():
    commands = [["ls"], ["date"], ["ps", "-l"]]
    for cmd in commands:
        pid = os.fork()
        if pid == 0:
            print(f"\nExecuting command {cmd} in Child PID={os.getpid()}")
            os.execvp(cmd[0], cmd)
    for i in range(len(commands)):
        os.wait()
