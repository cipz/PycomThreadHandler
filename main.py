import time
from ThreadHandler import *

def main():

    # Starting threads
    for i in range(0,3):
        startExampleThread(i)
        time.sleep(1)

    # Stopping threads
    for j in range(0,3):
        stopExampleThread(j)
        time.sleep(1)

if __name__ == "__main__":
    main()