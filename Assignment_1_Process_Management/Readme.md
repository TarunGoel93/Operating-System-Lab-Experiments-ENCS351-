```markdown
# Assignment 1: Process Creation and Management Using Python OS Module

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![OS](https://img.shields.io/badge/OS-Linux-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## Course Details
- **Course Code & Name**: ENCS351 Operating System  
- **Program Name**: B.Tech CSE, AI/ML, Data Science, Cybersecurity, FSD, UX/UI  
- **Submission**: Individual submission via LMS with GitHub link  
- **Experiment**: Lab Experiment Sheet-1  

---

## Table of Contents
- [Experiment Overview](#experiment-overview)
- [Learning Objectives](#learning-objectives)
- [Folder Structure](#folder-structure)
- [Task Descriptions](#task-descriptions)
  - [Task 1: Process Creation Utility](#task-1-process-creation-utility)
  - [Task 2: Command Execution Using exec()](#task-2-command-execution-using-exec)
  - [Task 3: Zombie & Orphan Processes](#task-3-zombie--orphan-processes)
  - [Task 4: Inspecting Process Info from /proc](#task-4-inspecting-process-info-from-proc)
  - [Task 5: Process Prioritization](#task-5-process-prioritization)
- [Dependencies](#dependencies)
- [How to Run Locally](#how-to-run-locally)
- [Expected Outcomes](#expected-outcomes)
- [Complexity Analysis](#complexity-analysis)
- [Practical Applications](#practical-applications)
- [Author](#author)
- [References](#references)

---

## Experiment Overview
This assignment simulates Linux process management using Python, focusing on:
- **Process creation** using `os.fork()`
- **Command execution** with `os.execvp()` or `subprocess.run()`
- **Parent-child relationships**
- **Zombie and orphan processes**
- **Process inspection** via `/proc`
- **Process prioritization** using `nice()` values

> **Note**: This project must be run on a Linux-based OS for full functionality due to the use of `/proc` and process-related system calls.

---

## Learning Objectives
- Understand the lifecycle of processes in Linux
- Create child processes and execute system commands using Python
- Simulate zombie and orphan processes
- Inspect running processes using `/proc`
- Demonstrate priority scheduling using `nice()` values

---

## Folder Structure
```
Assignment_1_Process_Management/
├── task1_process_creation.py   # Creates N child processes and prints PID/PPID
├── task2_exec_command.py       # Executes Linux commands in child processes
├── task3_zombie_orphan.py      # Simulates zombie and orphan processes
├── task4_proc_inspection.py     # Inspects process details from /proc/[pid]
├── task5_priority.py           # Assigns nice values and observes execution order
├── process_management.py       # Main script to run all tasks sequentially
├── output.txt                  # Combined outputs of all tasks
├── report.pdf                  # Summary report with code snapshots and results
└── README.md                   # This file
```

---

## Task Descriptions

### Task 1: Process Creation Utility
- **Objective**: Create `N` child processes using `os.fork()`.
- **Details**:
  - Each child process prints:
    - Its Process ID (PID)
    - Its Parent Process ID (PPID)
    - A custom message
  - The parent process waits for all children using `os.wait()`.
- **Output**: Process tree with PIDs and PPIDs logged to `output.txt`.

### Task 2: Command Execution Using exec()
- **Objective**: Modify Task 1 to execute Linux commands in child processes.
- **Details**:
  - Each child executes a command like `ls`, `date`, or `ps`.
  - Uses `os.execvp()` or `subprocess.run()`.
- **Output**: Command outputs logged to `output.txt`.

### Task 3: Zombie & Orphan Processes
- **Objective**: Simulate zombie and orphan processes.
- **Details**:
  - **Zombie**: Fork a child and skip `os.wait()` in the parent to create a zombie process.
  - **Orphan**: Parent exits before the child completes, leaving the child as an orphan.
  - Verify using `ps -el | grep defunct`.
- **Output**: Logs of zombie/orphan process states in `output.txt`.

### Task 4: Inspecting Process Info from /proc
- **Objective**: Retrieve and display process details for a given PID.
- **Details**:
  - Reads from `/proc/[pid]/status` for:
    - Process name
    - State
    - Memory usage
  - Reads from `/proc/[pid]/exe` for the executable path.
  - Lists open file descriptors from `/proc/[pid]/fd`.
- **Output**: Process details logged to `output.txt`.

### Task 5: Process Prioritization
- **Objective**: Demonstrate process scheduling using `nice()` values.
- **Details**:
  - Create multiple CPU-intensive child processes.
  - Assign different `nice()` values to each child.
  - Log execution order to show the impact of scheduling priority.
- **Output**: Execution order and nice values logged to `output.txt`.

---

## Dependencies
- **Python**: 3.x
- **Operating System**: Linux-based (e.g., Ubuntu, required for `/proc` and process simulation)
- **Python Modules**:
  - `os`
  - `subprocess`
  - `time`
  - `sys`

> **Warning**: This project will not work fully on non-Linux systems (e.g., Windows or macOS) due to the absence of `/proc`.

---

## How to Run Locally
1. **Clone the repository**:
   ```bash
   git clone <your-github-repo-link>
   cd Assignment_1_Process_Management
   ```
2. **Run all tasks**:
   ```bash
   python3 process_management.py
   ```
   - This executes all tasks sequentially and appends outputs to `output.txt`.

3. **Run individual tasks** (optional):
   ```bash
   python3 task1_process_creation.py
   python3 task2_exec_command.py
   python3 task3_zombie_orphan.py
   python3 task4_proc_inspection.py
   python3 task5_priority.py
   ```

4. **Verify zombie/orphan processes** (Task 3):
   ```bash
   ps -el | grep defunct
   ```

5. **Check output**:
   - Combined outputs are saved in `output.txt`.
   - Individual task outputs are printed to the console and appended to `output.txt`.

---

## Expected Outcomes
- **Task 1**: Child-parent process tree displayed with PIDs and PPIDs.
- **Task 2**: Linux commands executed successfully by child processes.
- **Task 3**: Zombie and orphan processes observed via `ps -el | grep defunct`.
- **Task 4**: Process details (name, state, memory, executable path, file descriptors) retrieved from `/proc`.
- **Task 5**: Execution order reflects the impact of different `nice()` values.

> **Tip**: Review `output.txt` for detailed logs and include snapshots in `report.pdf`.

---

## Complexity Analysis
- **Time Complexity**: O(n) for creating and managing `n` processes.
- **Space Complexity**: O(n) for storing process IDs and logs.

---

## Practical Applications
- Operating system kernel development
- Performance tuning via process scheduling
- Real-time and embedded system programming
- Debugging and process monitoring tools

---

## Author
- **Name**: Tarun Goel  
- **Program**: B.Tech CSE  
- **Experiment**: Lab Experiment Sheet-1, ENCS351 Operating System  

---

## References
- [Python Official Documentation: os module](https://docs.python.org/3/library/os.html)
- [Python Official Documentation: subprocess module](https://docs.python.org/3/library/subprocess.html)
- [Linux Process Management Concepts](https://man7.org/linux/man-pages/man7/)
```

This README.md includes all the required details in a professional, GitHub-friendly format with badges, a table of contents, and clear instructions for running the project locally. Let me know if you need the Python code for the tasks or any other modifications!