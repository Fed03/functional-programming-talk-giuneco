from functools import partial 
from inspect import signature

def add(x,y):
  return x+y


def curry(fn):
  arity = len(signature(fn).parameters)
  def _curry(*args):
    if len(args) < arity:
      return partial(_curry, *args)
    return fn(*args)
  
  return _curry


adC = curry(add)
add3 = adC(3)
print(add3(2))