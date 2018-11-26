from functools import partial, reduce
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


def call(args, fn):
    try:
        args = iter(args)
    except TypeError:
        args = (args,)
    return fn(*args)


def compose(*fns):
    def _composed(*args):
        val = reduce(call, reversed(fns), args)
        return val

    return _composed
