import time

def set_func(fun):
    def call_func():
        start_time=time.time()
        func()
        stop_time=time.time()
        print("alltime is %f"%(stop_time-start_time))
    return call_func

@set_func
def test1():
    print("---test---")
    for i in range(10000):
        pass

test1()
test1()
