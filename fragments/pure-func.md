# Let's get @color[#4487f2](Pure)
+++
The foundations of FP are the so called @color[#4487f2](pure) functions.
<br><br><br>
A function is @color[#4487f2](pure) if it follows some policies that relates it closely to the concept of math functions.
+++
@snap[north-west]
@color[#4487f2](Pure) Function Policies
@snapend

@snap[west list-content-concise span-100]
@ol
- Works only with its input (no access to outer context)
- Must have at least 1 arg (0-arity not allowed)
- Should be called with 1 arg (more on this later)
- Must return an output
- Must declare its dependencies through parameters
- Without side-effects
@olend
@snapend
+++
#### Not pure
```python
number = 5
def add5(x):
  return number + x
```
+++
#### Also not pure
```python
def just10():
  return 10
```
+++
#### Neither this
```python
def addNoReturn(x, y):
  z = x + y
```
+++
@snap[north]
### Pure functions are @color[#f26225](deterministic)
@snapend

@box[bg-orange text-white](Given points 1,2,3,4, all pure functions will always produce the same output when called with the same inputs)
+++
#### Determinism is what makes @color[#4487f2](pure) functions equivalent to the math ones

<br>

This equivalence will allow us to use powerful math tools when structuring our softwares.
+++
#### This is @color[#4487f2](Pure)!
```python
def add(x, y):
  return x + y

print(add(1, 2)) # prints 3
print(add(1, 2)) # still prints 3
print(add(1, 2)) # WILL ALWAYS print 3
```
