import threading

def work():
    print("Thread is working")

t1 = threading.Thread(target=work)
t1.start()

t1.join()

print("Main thread continues")