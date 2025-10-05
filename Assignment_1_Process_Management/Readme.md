Assignment 1: Process Creation and Management Using Python OS Module

Course Information
    Course Code & Title: ENCS351 Operating Systems
    Program: B.Tech in Computer Science and Engineering 
    Submission: Individual submission via Learning Management System (LMS) with GitHub repository link
    Experiment: Lab Experiment Sheet-1, Process Management

Overview
    This assignment focuses on simulating Linux process management using Python, providing practical exposure to core operating system concepts. It covers:
        - Process creation using os.fork()
        - Command execution with os.execvp() or subprocess.run()
        - Parent-child process relationships
        - Simulation of zombie and orphan processes
        - Process inspection via /proc filesystem
        - Process prioritization using nice() values

Learning Outcomes
    - Understand the lifecycle of processes in a Linux environment
    - Create and manage child processes using Python
    - Simulate and verify zombie and orphan processes
    - Retrieve and analyze process information from /proc
    - Demonstrate the impact of process prioritization using nice() values

Project Structure
    Assignment_1_Process_Management/
    ├── task1_process_creation.py   # Creates N child processes and prints PID/PPID
    ├── task2_exec_command.py       # Executes Linux commands in child processes
    ├── task3_zombie_orphan.py      # Simulates zombie and orphan processes
    ├── task4_proc_inspection.py     # Inspects process details from /proc/[pid]
    ├── task5_priority.py           # Assigns nice values and observes execution order
    ├── process_management.py       # Main script to run all tasks sequentially
    ├── output.txt                  # Combined outputs of all tasks
    ├── report.pdf                  # Summary report with code snapshots and results
    └── README.md                   # Project documentation

Task Descriptions

    Task 1: Process Creation Utility
        Objective: Create N child processes using os.fork()
        Details:
            - Each child process prints:
                - Process ID (PID)
                - Parent Process ID (PPID)
                - A custom message
            - Parent process waits for all children using os.wait()
        Output: Process tree with PIDs and PPIDs logged to output.txt

    Task 2: Command Execution Using exec()
        Objective: Execute Linux commands in child processes
        Details:
            - Each child executes a command (e.g., ls, date, ps)
            - Uses os.execvp() or subprocess.run()
        Output: Command outputs logged to output.txt

    Task 3: Zombie and Orphan Processes
        Objective: Simulate zombie and orphan processes
        Details:
            - Zombie: Fork a child and skip os.wait() in the parent
            - Orphan: Parent exits before the child completes
            - Verify using: ps -el | grep defunct
        Output: Logs of zombie/orphan process states in output.txt

    Task 4: Process Inspection via /proc
        Objective: Retrieve and display process details for a given PID
        Details:
            - Reads from /proc/[pid]/status for:
                - Process name
                - State
                - Memory usage
            - Reads from /proc/[pid]/exe for executable path
            - Lists open file descriptors from /proc/[pid]/fd
        Output: Process details logged to output.txt

    Task 5: Process Prioritization
        Objective: Demonstrate process scheduling using nice() values
        Details:
            - Create multiple CPU-intensive child processes
            - Assign different nice() values to each child
            - Log execution order to show scheduling priority impact
        Output: Execution order and nice values logged to output.txt

Dependencies
    - Python: 3.x
    - Operating System: Linux-based (e.g., Ubuntu, required for /proc and process simulation)
    - Python Modules:
        - os
        - subprocess
        - time
        - sys
    Note: This project requires a Linux environment due to reliance on /proc and Linux-specific system calls.

Setup and Execution
    1. Clone the repository:
       git clone <your-github-repo-link>
       cd Assignment_1_Process_Management
    2. Run all tasks:
       python3 process_management.py
       - Executes all tasks sequentially and appends outputs to output.txt
    3. Run individual tasks (optional):
       python3 task1_process_creation.py
       python3 task2_exec_command.py
       python3 task3_zombie_orphan.py
       python3 task4_proc_inspection.py
       python3 task5_priority.py
    4. Verify zombie/orphan processes (Task 3):
       ps -el | grep defunct
    5. Check output:
       - Combined outputs are saved in output.txt
       - Individual task outputs are printed to the console and appended to output.txt

Expected Results
    - Task 1: Child-parent process tree displayed with PIDs and PPIDs
    - Task 2: Linux commands executed successfully by child processes
    - Task 3: Zombie and orphan processes observed via ps -el | grep defunct
    - Task 4: Process details (name, state, memory, executable path, file descriptors) retrieved from /proc
    - Task 5: Execution order reflects the impact of different nice() values

Complexity Analysis
    - Time Complexity: O(n) for creating and managing n processes
    - Space Complexity: O(n) for storing process IDs and logs

Applications
    - Operating system kernel development
    - Performance tuning via process scheduling
    - Real-time and embedded system programming
    - Debugging and process monitoring tools

Author
    Name: Tarun Goel
    Program: B.Tech CSE
    Experiment: Lab Experiment Sheet-1, ENCS351 Operating System

References
    - Python Official Documentation: os module (https://docs.python.org/3/library/os.html)
    - Python Official Documentation: subprocess module (https://docs.python.org/3/library/subprocess.html)
    - Linux Process Management Concepts (https://man7.org/linux/man-pages/man7/)
