import multiprocessing
import os
import time

def child_task():
    print(f"Child process ID: {os.getpid()}")
    print("Child is doing some work...")
    time.sleep(2)
    print("Child process finished.")

if __name__ == "__main__":
    print(f"Parent process ID: {os.getpid()}")
    

    p = multiprocessing.Process(target=child_task)
    
    p.start()
    
    p.join()
    
    print("Parent process is exiting.")