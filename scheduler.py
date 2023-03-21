def FCFS():

    n = int(input("Enter the number of processes: "))
    arrival_time = list(map(int, input("Enter the arrival time of the processes separated by spaces: ").split()))
    burst_time = list(map(int, input("Enter the burst time of the processes separated by spaces: ").split()))

    execution_sequence = [] # list to store the execution sequence of processes
    waiting_time = [0] * n  # list to store the waiting time for each process
    total_waiting_time = 0  # variable to store the total waiting time
    
    for i in range(n):
        if i == 0:
            execution_sequence.append(1) # first process is always executed first
            waiting_time[i] = 0          # waiting time for first process is always 0
        else:
            execution_sequence.append(i+1) # next process is executed
            waiting_time[i] = burst_time[i-1] + waiting_time[i-1] - arrival_time[i] # calculate waiting time for current process
            total_waiting_time += waiting_time[i] # add the waiting time to the total waiting time
    
    # calculate the average waiting time
    avg_waiting_time = total_waiting_time/n

    print("Process execution sequence: ", execution_sequence)
    print("Average waiting time: ", avg_waiting_time)

def SRTF():

    n = int(input("Enter the number of processes: "))
    arrival_time = list(map(int, input("Enter the arrival time of the processes separated by spaces: ").split()))
    burst_time = list(map(int, input("Enter the burst time of the processes separated by spaces: ").split()))
    # Create a process list with process id, arrival time, and burst time
    process_list = [[i, arrival_time[i], burst_time[i]] for i in range(n)]
    waiting_time = [0] * n
    process_list.sort(key=lambda x: x[1]) # Sort the process list based on the arrival time
    current_time = 0
    remaining_processes = n
    execution_sequence = []

    while remaining_processes:
        # Find the shortest process that has arrived
        shortest_process = min((i for i in range(n) if process_list[i][1] <= current_time and process_list[i][2]),
                                default=-1, key=lambda i: process_list[i][2])
        # If no processes arrived yet, increase the current time and continue the loop
        if shortest_process == -1:
            current_time += 1
            continue
        process_list[shortest_process][2] -= 1
        current_time += 1
        execution_sequence.append(process_list[shortest_process][0] + 1) # Add the executed process to the sequence
        # If the burst time of the shortest process reaches 0, decrement the remaining processes
        # and calculate the waiting time for this process
        if process_list[shortest_process][2] == 0:
            remaining_processes -= 1
            finish_time = current_time
            waiting_time[shortest_process] = finish_time - arrival_time[shortest_process] - burst_time[shortest_process]
            # If the last process to execute finished, remove duplicates from the execution sequence
            if remaining_processes == 0:
                execution_sequence = list(dict.fromkeys(execution_sequence))

    avg_waiting_time = sum(waiting_time) / n
    print("Execution sequence: ", execution_sequence)
    print("Average waiting time: ", avg_waiting_time)

def priority():

    n = int(input("Enter the number of processes: "))
    at = list(map(int, input("Enter the arrival time of the processes separated by spaces: ").split()))
    bt = list(map(int, input("Enter the burst time of the processes separated by spaces: ").split()))
    pr = list(map(int, input("Enter the priority of the processes separated by spaces: ").split()))
    t = 0
    complete = [False] * n # Initialize completion array to False for all processes
    check = False
    minm = float('inf')    # Initialize minimum priority to infinity
    tat = [0] * n
    wt = [0] * n
    bt_original = bt[:]    # Save the original burst time
    sequence = []          # Initialize the sequence list

    while not all(complete):
        # Check for arrival of processes and find the one with minimum priority that has not yet been completed
        for i in range(n):
            if at[i] <= t and pr[i] < minm and not complete[i]:
                minm = pr[i]
                shortest = i
                check = True
        # If no process has arrived yet, increment time
        if not check:
            t += 1
            continue
        bt[shortest] -= 1
        minm = float('inf') # Reset minimum priority to infinity
        # If the current process has completed
        if bt[shortest] == 0:
            complete[shortest] = True
            check = False
            end_time = t + 1
            tat[shortest] = end_time - at[shortest]
            wt[shortest] = tat[shortest] - bt_original[shortest]
            sequence.append(shortest)  # Add the completed process index to the sequence list
        # Increment time
        t += 1

    avg_wt = sum(wt) / n
    print("Average waiting time: ", avg_wt)
    print("Execution sequence: ", sequence)

def round_robin():
    # Get input
    total_p_no = int(input("Enter Total Process Number: "))
    proc = []
    for i in range(total_p_no):
        arrival, burst = map(int, input("Enter process arrival time and burst time: ").split())
        proc.append([arrival, burst, burst, 0])

    time_quantum = int(input("Enter time quantum: "))

    # Run round-robin scheduling
    process_order = []
    total_time = 0
    wait_time = 0
    turnaround_time = 0
    while any(proc[i][2] > 0 for i in range(total_p_no)):
        for i in range(total_p_no):
            if proc[i][2] <= time_quantum and proc[i][2] > 0:
                total_time += proc[i][2]
                process_order.append(i)
                wait_time += total_time - proc[i][0] - proc[i][1]
                turnaround_time += total_time - proc[i][0]
                proc[i][2] = 0
            elif proc[i][2] > 0:
                total_time += time_quantum
                process_order.append(i)
                proc[i][2] -= time_quantum

            # Print output
            print(f"Avg Waiting Time: {wait_time / total_p_no}")
            print(f"Process sequence: {process_order}")

def main():
    while True:
        print("1. First-Come, First-Served (FCFS) scheduling")
        print("2. Shortest Remaining Time First (SRTF) scheduling")
        print("3. Priority scheduling")
        print("4. Round Robin scheduling")
        print("5. Quit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            FCFS()
        elif choice == 2:
            SRTF()
        elif choice == 3:
            priority()
        elif choice == 4:
            round_robin()
        elif choice == 5:
            break
        else:
            print("Invalid choice! Please try again.")

# Call the main function
if __name__ == '__main__':
    main()