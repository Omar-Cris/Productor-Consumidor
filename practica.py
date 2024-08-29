import threading
import time
import random
from collections import deque
from threading import Semaphore

BUFFER_SIZE = 10
buffer = deque(maxlen=BUFFER_SIZE)

empty = Semaphore(BUFFER_SIZE)  
full = Semaphore(0)  
mutex = Semaphore(1)  

def producer():
    while True:
        item = random.randint(1, 100) 
        empty.acquire() 
        mutex.acquire() 
        buffer.append(item) 
        print(f"Productor produjo: {item}")
        mutex.release()  
        full.release() 
        time.sleep(random.random())

def consumer():
    while True:
        full.acquire()  
        mutex.acquire()  
        item = buffer.popleft()  
        print(f"Consumidor consumió: {item}")
        mutex.release()  
        empty.release()  
        time.sleep(random.random())  


producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()
