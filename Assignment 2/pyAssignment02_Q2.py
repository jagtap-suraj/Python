#Python Assignment No. 02 (Q2)

"""Write a program to print current date using multithreading (create two threads)."""

import threading
import datetime

def print_date():

    print(f"Current date and time: {datetime.datetime.now()}")

if __name__ == "__main__":

    t1 = threading.Thread(target=print_date)
    t2 = threading.Thread(target=print_date)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
