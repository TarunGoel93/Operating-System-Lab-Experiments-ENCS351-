# Operating System Lab Experiments (ENCS351)
[![Ask DeepWiki](https://devin.ai/assets/askdeepwiki.png)](https://deepwiki.com/TarunGoel93/Operating-System-Lab-Experiments-ENCS351-)

This repository contains lab experiments for the ENCS351 Operating System course. The experiments explore fundamental OS concepts, including process management, scheduling, and concurrency, using Python.

## Experiments

### Assignment 1: Process Management in Linux

This assignment simulates core Linux process management functionalities using Python's `os` module. It provides hands-on experience with process lifecycle, execution, and resource management.

**Note:** This experiment must be run on a Linux-based operating system due to its reliance on the `/proc` filesystem and system calls like `os.fork()`.

#### Key Concepts Covered
- **Process Creation**: Using `os.fork()` to create child processes.
- **Command Execution**: Running system commands like `ls`, `date`, and `ps` within child processes using `os.execvp()`.
- **Parent-Child Synchronization**: Managing process termination with `os.wait()`.
- **Zombie & Orphan Processes**: Simulating and observing these special process states.
- **Process Inspection**: Reading process metadata (PID, PPID, state, memory) directly from the `/proc` filesystem.
- **Process Prioritization**: Modifying process scheduling priority using `os.nice()` and observing the impact on execution order.

#### Tasks
- **Task 1: Process Creation Utility**: Creates a user-specified number of child processes and prints their PID and PPID.
- **Task 2: Command Execution**: Demonstrates executing Linux commands in separate child processes.
- **Task 3: Zombie & Orphan Processes**: Creates scenarios to produce and identify zombie and orphan processes.
- **Task 4: Inspecting /proc**: Retrieves and displays detailed information about a given process by reading from `/proc/[pid]`.
- **Task 5: Process Prioritization**: Launches multiple CPU-intensive processes with different `nice` values to show the effect of priority on scheduling.

#### How to Run
1.  Navigate to the assignment directory:
    ```sh
    cd Assignment_1_Process_Management/
    ```
2.  Run the main script:
    ```sh
    python3 process_management.py
    ```
3.  Enter the number corresponding to the task you wish to execute.

### Assignment 2: Multiprocessing with Logging

This assignment demonstrates creating and managing concurrent processes using Python's `multiprocessing` library. It also incorporates the `logging` module to record the activity of each process to a file.

#### Key Concepts Covered
- **Process Instantiation**: Creating independent processes using `multiprocessing.Process`.
- **Concurrent Execution**: Starting processes to run in parallel with `process.start()`.
- **Process Synchronization**: Waiting for processes to complete their execution using `process.join()`.
- **Process-Safe Logging**: Using the `logging` module to write timestamped logs from multiple processes to a shared file.

#### Functionality
The main script, `script.py`, initializes a logger, creates two processes, and assigns each a simple task that involves a short delay. The start and end times of each process's task are logged to `process_log.txt`, and the main program waits for both to finish before shutting down.

#### How to Run
1.  Navigate to the assignment directory:
    ```sh
    cd Assignment_2/
    ```
2.  Run the script:
    ```sh
    python3 script.py
    ```
3.  Check the output:
    -   The terminal will display "System Starting..." and "System Shutdown."
    -   A `process_log.txt` file will be created with detailed logs from each process.
