# encoding=utf-8

import threading
import random
import time

gMoney = 1000
gLock = threading.Lock()
gTotalTimes = 10
gTimes = 0

class Producer(threading.Thread):
    def run(self):
        global gMoney
        global gTimes
        while True:
            money = random.randint(100,1000)
            gLock.acquire()
            if gTimes >=10:
                gLock.release()
                break
            gMoney += money
            print('%s生产了%d元钱,剩余%d元钱'%(threading.current_thread(),money,gMoney))
            gTimes +=1
            gLock.release()
            time.sleep(1)

class Consumer(threading.Thread):
    def run(self):
        global gMoney
        while True:
            money = random.randint(100,1000)
            gLock.acquire()
            if gMoney >= money:
                gMoney -=money
                print('%s消费者消费了%d元钱，剩余%d元钱'%(threading.current_thread(),money,gMoney))
            gLock.release()
            time.sleep(0.5)

def main():
    for x in range(3):
        t = Consumer(name='消费着线程%d'%x)
        t.start()
    for x in range(5):
        t = Producer(name='生产者线程%d'%x)
        t.start()

if __name__ == '__main__':
    main()
