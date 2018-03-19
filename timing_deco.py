#decorator demo
import time

def time_it(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)  
        end = time.time()
        print(func.__name__ + ' took ' + str(end-start) + ' to excecute')
    return wrapper
    
@time_it        
def loo():
    d = range(0,1000)
    time.sleep(3)
    print(d)
        

        
        
loo()
