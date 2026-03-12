# Activity 2.7 – CPU Scheduling Metrics

processes = ["P1", "P2", "P3"]
arrival_time = [0, 1, 2]
burst_time = [4, 3, 5]

n = len(processes)

completion_time = [0] * n
turnaround_time = [0] * n
waiting_time = [0] * n

# FCFS Scheduling
completion_time[0] = arrival_time[0] + burst_time[0]

for i in range(1, n):
    completion_time[i] = completion_time[i-1] + burst_time[i]

# Calculate Turnaround and Waiting Time
for i in range(n):
    turnaround_time[i] = completion_time[i] - arrival_time[i]
    waiting_time[i] = turnaround_time[i] - burst_time[i]

print("\nProcess  AT  BT  CT  TAT  WT")
for i in range(n):
    print(processes[i], "   ", arrival_time[i], " ", burst_time[i], " ", completion_time[i], " ", turnaround_time[i], " ", waiting_time[i])

# CPU Utilization
cpu_busy = sum(burst_time)
total_time = completion_time[-1]

cpu_utilization = (cpu_busy / total_time) * 100

print("\nCPU Utilization:", round(cpu_utilization,2), "%")