#threading
import time
start=time.perf_counter()
def calculateTime():
    print("sleep for 5 second")
    time.sleep(5)
    print("completed sleeep")
calculateTime()
calculateTime()
calculateTime()
finish=time.perf_counter()
print(f'Finished in {finish-start} seconds')

#############################################################

import threading
import time
start=time.perf_counter()
def calculateTime():
    print("sleep for 5 second")
    time.sleep(5)
    print("completed sleeep")
t1=threading.Thread(target=calculateTime)
t2=threading.Thread(target=calculateTime)
t3=threading.Thread(target=calculateTime)
t4=threading.Thread(target=calculateTime)
t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()

finish=time.perf_counter()
print(f'Finished in {finish-start} seconds')

#################################################

import threading
import time
start=time.perf_counter()
def calculateTime():
    print("sleep for 5 second")
    time.sleep(5)
    print("completed sleeep")
threads=[]
for _ in range(5):
    thread=threading.Thread(target=calculateTime)
    thread.start()
    threads.append(thread)
for t in threads:
    t.join()

finish=time.perf_counter()
print(f'Finished in {finish-start} seconds')
############################################

import threading
import time
start=time.perf_counter()
def calculateTime(seconds):
    print(f"sleep for {seconds} 5 second")
    time.sleep(5)
    print(f"completed {seconds} sleeep")
threads=[]
for _ in range(5):
    thread=threading.Thread(target=calculateTime,args=[3])
    thread.start()
    threads.append(thread)
for t in threads:
    t.join()

finish=time.perf_counter()
print(f'Finished in {finish-start} seconds')

#concurrency

import concurrent.futures
import time
start=time.perf_counter()
def calculateTime(seconds):
    print(f"sleep for {seconds} second \n")
    time.sleep(seconds)
    return f"completed {seconds} sleep \n"
with concurrent.futures.ThreadPoolExecutor() as executor:
    l=[4,6,3,2]
    results=[executor.submit(calculateTime,i) for i in l]
    '''for _ in range(5):
        thread = threading.Thread(target=calculateTime, args=[3])
        thread.start()
        threads.append(thread)
    for t in threads:
        t.join()'''
    for r in concurrent.futures.as_completed(results):
        print(r.result())
finish=time.perf_counter()
print(f'Finished in {finish-start} seconds')
