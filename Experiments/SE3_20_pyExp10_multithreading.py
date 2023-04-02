# SE-3, 20, Suraj Jagtap

#Python Experiment No. 10

"""Every day several people want a reservation for a seat berth in a train. 
Let's think that only one birth is available and two passengers (threads) are asking for that birth. 
Let's assume that in reservation counter no.1, the clerk has sent a request to the server to allot that berth to his passenger. 
In counter no.2, the second clerk has also sent a request to the server to allot that birth to his passenger. 
It means two passengers are competing for the same birth. 
Write a Python program to ensure that seat is allotted to only one passenger using synchronization methods."""

from threading import *
from time import *

sema = Semaphore()

class Railway:
    def __init__(self, available):
        self.available = available
        self.lock = Lock()

    def reserve(self, wanted):
        self.lock.acquire()
        print("Available no. of berths:", self.available)
        name = current_thread().name
        if self.available >= wanted:
            print("%d berths allotted for %s" % (wanted, name))
            sleep(1.5)
            self.available -= wanted
        else:
            print("Sorry, no berths to allot")
        self.lock.release()

obj = Railway(1)

t1 = Thread(target=obj.reserve, args=(1,))
t2 = Thread(target=obj.reserve, args=(1,))

t1.name = 'First Person'
t2.name = 'Second Person'

t1.start()
t2.start()