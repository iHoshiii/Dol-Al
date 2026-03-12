import turtle
import time

# Process data
processes = ["P1", "P2", "P3", "P4"]
burst_time = [5, 3, 8, 6]
priority = [2, 1, 3, 2]

quantum = 2

# Turtle setup
screen = turtle.Screen()
screen.title("CPU Scheduling Simulation")

pen = turtle.Turtle()
pen.speed(0)
pen.penup()

y = 100

# Draw initial processes
def draw_processes():
    global y
    for i in range(len(processes)):
        pen.goto(-300, y)
        pen.write(processes[i], font=("Arial", 12, "bold"))
        
        pen.goto(-250, y)
        pen.pendown()
        for j in range(burst_time[i]):
            pen.forward(20)
        pen.penup()
        y -= 40

# Round Robin Simulation
def round_robin():
    bt = burst_time.copy()
    x = -250
    y = -100
    
    while True:
        done = True
        
        for i in range(len(bt)):
            if bt[i] > 0:
                done = False
                
                pen.goto(x, y)
                pen.write(processes[i], font=("Arial", 10, "normal"))
                
                execute = min(quantum, bt[i])
                
                pen.goto(x, y-10)
                pen.pendown()
                pen.forward(20 * execute)
                pen.penup()
                
                x += 20 * execute
                bt[i] -= execute
                
                time.sleep(0.5)
        
        if done:
            break

# Priority Scheduling Simulation
def priority_scheduling():
    pen.goto(-300, -200)
    pen.write("Priority Scheduling", font=("Arial", 12, "bold"))
    
    order = sorted(range(len(processes)), key=lambda i: priority[i])
    
    x = -250
    y = -220
    
    for i in order:
        pen.goto(x, y)
        pen.write(processes[i], font=("Arial", 10, "normal"))
        
        pen.goto(x, y-10)
        pen.pendown()
        pen.forward(20 * burst_time[i])
        pen.penup()
        
        x += 20 * burst_time[i]
        time.sleep(0.5)

# Run simulation
draw_processes()

pen.goto(-300, -80)
pen.write("Round Robin", font=("Arial", 12, "bold"))

round_robin()

priority_scheduling()

turtle.done()