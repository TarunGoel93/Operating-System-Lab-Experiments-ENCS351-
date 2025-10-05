# process_management.py

from task1_process_creation import task1
from task2_exec_command import task2
from task3_zombie_orphan import task3
from task4_proc_inspection import task4
from task5_priority import task5

if __name__ == "__main__":
    print("Select Task to Run:")
    print("1. Process Creation")
    print("2. Command Execution")
    print("3. Zombie & Orphan Processes")
    print("4. Process Info from /proc")
    print("5. Process Prioritization")

    choice = int(input("Enter task number (1-5): "))
    if choice == 1:
        task1()
    elif choice == 2:
        task2()
    elif choice == 3:
        task3()
    elif choice == 4:
        task4()
    elif choice == 5:
        task5()
    else:
        print("Invalid choice.")
