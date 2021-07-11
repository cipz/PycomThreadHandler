import time
import _thread

# By using a global variable that 
THREAD_KILL_SWITCH = dict()

# THREAD_KILL_SWITCH[thread_id] = False --> Thread continues executing
# THREAD_KILL_SWITCH[thread_id] = True  --> Thread will exit next time 

def startExampleThread(thread_id):
    global THREAD_KILL_SWITCH
    THREAD_KILL_SWITCH[thread_id] = False

    print("Starting thread {}".format(thread_id))

    _thread.start_new_thread(exampleThread, (thread_id, ))

def stopExampleThread(thread_id):
    global THREAD_KILL_SWITCH
    THREAD_KILL_SWITCH[thread_id] = True

    print("Stopping thread {}".format(thread_id))

def exampleThread(thread_id):
    global THREAD_KILL_SWITCH
    while not THREAD_KILL_SWITCH[thread_id]:

        print("This thread has id {}".format(thread_id))
        time.sleep(2)