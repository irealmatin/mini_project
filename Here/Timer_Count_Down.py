import time

def count_down(tm):
    """
    this function get a time in seconds form and count down that numbar in a form like  this -> 00:00
    """
    while tm :
        minutes , seconds = divmod(tm,60) # this give us a tuple with 2 index. first one min second one secs
        timer = '{:02d}:{:02d}'.format(minutes,seconds) 
        print(timer , end = '\r')
        time.sleep(1)
        tm -= 1

    print("Time is over!!")

inp = int(input("write the time in second : "))
count_down(inp)
