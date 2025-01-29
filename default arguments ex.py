import time


def count (end,start=0):
    for x in range (start,end):
        print(x)
        time.sleep(1)   #1 sec delay
    print("DONE!")

#count(0,10) passing start and end parameters
#count(10)  setting start default argument to be zero and passing end parameter

