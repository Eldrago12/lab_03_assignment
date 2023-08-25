class Process:
    def __init__(self, p_id, process, start_time, priority):
        self.p_id = p_id
        self.process = process
        self.start_time = start_time
        self.priority = priority

def display_processes(processes):
    print("P_ID\tProcess\t\tStart Time\tPriority")
    print("--------------------------------------------")
    for process in processes:
        print(f"{process.p_id}\t{process.process}\t\t{process.start_time}\t\t{process.priority}")

def sort_by_process_id(processes):
    return sorted(processes, key=lambda x: x.p_id)

def sort_by_start_time(processes):
    return sorted(processes, key=lambda x: x.start_time)

def sort_by_priority(processes):
    return sorted(processes, key=lambda x: x.priority)

def main():
    processes = [
        Process("P1", "VSCode", 100, "High"),
        Process("P23", "Eclipse", 234, "MID"),
        Process("P93", "Chrome", 7, "High"),
        Process("P42", "JDK", 234, "MID"),
        Process("P9", "CMD", 189, "High"),
        Process("P87", "NotePad", 23, "Low")
    ]

    while True:
        print("\nMenu:")
        print("1. Sort by Process ID")
        print("2. Sort by Start Time")
        print("3. Sort by Priority")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            sorted_processes = sort_by_process_id(processes)
            display_processes(sorted_processes)
        elif choice == "2":
            sorted_processes = sort_by_start_time(processes)
            display_processes(sorted_processes)
        elif choice == "3":
            sorted_processes = sort_by_priority(processes)
            display_processes(sorted_processes)
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
