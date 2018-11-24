# Immutability is the new @color[#1dc579](black)
+++
```python
x = 5
x = x + 2
```
<br>
<br>
@quote[Forget math class! This is allowed in programming!](Any imperative programming tutorial)
+++
## In FP it is @color[red](illegal)!
<br>
There are no variables in FP

Only constants
+++
Luckly, "variables" are short living because they exist only inside functions.
<br><br>
@size[1.5em](And functions are small, right?)
+++
@size[1.9em](So...)
+++?image=assets/deadpool.jpg&position=left&size=55% 100%
@snap[east span-30]
@quote[How the hell am I supposed to do anything without vars?!?!]
@snapend
+++
@snap[north-west]
#### We edit vars only for 2 reasons
@snapend

@snap[west list-content-concise span-100]
@ol[fragment](false)
- Multi-valued changes (i.e. object properties or array elements, list, ...)
- Single-valued changes (i.e. loop counters)
@olend
@snapend
+++
@snap[north-west]
#### Solutions
@snapend
@box[bg-orange text-white demo-box-pad](Multi-valued changes#Everytime you need to change an object, create a copy with the updated values)
<br>
@box[bg-orange text-white demo-box-pad](Single-valued changes#Exactly in the same way, copying. And without using any loops!)
+++
### What? No loops?!?!

Hold on!

It's not like we can't do loops, it's just that there are no specific loop constructs like @color[goldenrod](**for**), @color[goldenrod](**while**), @color[goldenrod](**do**), etc.
+++
### We use recursion!
```python
acc = 0
for i in range(10):
    acc = acc + i

print(acc) # prints 45

def sumRange(start, end, acc):
    if start >= end:
        return acc
    return sumRange(start + 1, end, acc + start)

print(sumRange(0, 10, 0)) # prints 45
```
@[1-6](Simple loop construct)
@[7-12](Without loop construct or variables (recursion))
