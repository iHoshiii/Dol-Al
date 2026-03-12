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
    
    # Create the child process
    p = multiprocessing.Process(target=child_task)
    
    # Start the process
    p.start()
    
    # Wait for the child to finish (like a 'wait' in Unix)
    p.join()
    
    print("Parent process is exiting.")