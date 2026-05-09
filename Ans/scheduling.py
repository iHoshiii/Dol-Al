# Activity 2.8 – Real-Time Scheduling (EDF)

tasks = [
    {"name": "T1", "execution": 2, "deadline": 5},
    {"name": "T2", "execution": 1, "deadline": 3},
    {"name": "T3", "execution": 2, "deadline": 7}
]

# Sort tasks by deadline
tasks.sort(key=lambda x: x["deadline"])

time = 0

print("\nExecution Order (Earliest Deadline First):\n")

for task in tasks:
    start = time
    finish = time + task["execution"]
    
    print(task["name"], "Start:", start, "Finish:", finish, "Deadline:", task["deadline"])
    
    if finish <= task["deadline"]:
        print("Deadline Met\n")
    else:
        print("Deadline Missed\n")
    
    time = finish