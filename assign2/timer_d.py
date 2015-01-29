'''
Nathan Cazell (ntc10)
1/28/15
'''

from __future__ import print_function
import time

def t_decorator(func):
  def func_wrapper():
    start = time.time()
    func()
    end = time.time()
    print('Time to execute function (s) : ', (end - start))
  return func_wrapper
