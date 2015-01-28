import timer_d
import time

def myfunc():
  time.sleep(5)

mytimedfunc = timer_d.t_decorator(myfunc)
mytimedfunc()
