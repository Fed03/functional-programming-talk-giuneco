## Functional Programming
### & @color[#f26225](Lambdas)
---
@snap[north-west]
### We will scratch only the surface of FP
@snapend

@snap[west]
@ol[list-content-concise span-100](false)
- Pure functions
- Immutability
- Higher Order functions
- Currying
- Composition
@olend
@snapend
---
# @color[#f26225](DISCLAIMER)
---?image=assets/bg/orange.jpg&position=top&size=100% 20%
@snap[north span-100]
@size[1.5em](DISCLAIMER)
@snapend

@ul
- Learning FP is like starting from scratch
- We will start over from square zero
- I am no expert in Functional Programming
- There will be a little bit of @color[firebrick](math) concepts
@ulend
---
# @color[firebrick](MATH?!?!)
![angry](assets/angry-brian-opt.gif)
---
@snap[north-west]
### Yes, @color[firebrick](Math).
@snapend

@snap[west snap-100]
<p>Functional programming bases its reasoning around math concepts.</p>
@ul[](false)
- Functions (the math ones)
- Sets theory
- Categories theory
- @color[#f26225](Lambda) calculus
@ulend
@snapend
---?include=fragments/math-functions/PITCHME.md
---?include=fragments/pure-func.md
---
# @color[#9e35de](Side)-effects
+++
#### @color[#9e35de](Side)-effects represent the interactions with the world outside the function
+++
@snap[north-west]
@color[#9e35de](Side)-effects include, but are not limited to:
@snapend

@snap[west list-content-concise span-100]
@ul
- Changing the File-System
- Interacting with a Database
- Making an HTTP request
- Mutating an external state
- Printing to screen/console or logging
- Accessing the DOM
- Accessing the underlying system
@ulend
@snapend
+++
#### In imperative programming languages<br>(C#, Java, JS, ...), @color[#9e35de](side)-effects are everywhere

<br>

They make debugging really hard because anything can be potentially changed by anyone.
<br><br>
Where do you look for bugs?
---
#### So, at this point you're thinking...
+++?image=assets/doc-brown.jpg&size=cover
@snap[north-west span-35]
@quote[How the hell am I supposed to do anything useful with only pure functions?!?]
@snapend
+++?image=assets/bg/white.jpg&position=left&size=50% 100%
@snap[east split-screen-text text-white]
#### @color[#f26225](FP) is not only pure functions
@ul[split-screen-list](false)
- All useful SW has to interact with the outside world
- Try to confine @color[#9e35de](side)-effects
- Segregate impure code from @color[#4487f2](pure)
- Minimize the amount of impure code
@ulend
@snapend

@snap[west split-screen-fa]
@box[bg-orange text-white rounded](@fa[puzzle-piece fa-5x])
@snapend
---
# Immutability is the new @color[mediumaquamarine](black)
+++
```python
x = 5
x = x + 2
```
<br>
<br>
@quote[Forget math class! This is allowed in programming!](Any imperative programming tutorial)
+++
### In FP it is @color[red](illegal)!
+++
@box[bg-orange text-white rounded](There are no variables in FP<br><br> Only constants)
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
---
