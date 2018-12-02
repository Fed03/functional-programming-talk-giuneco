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
---?image=https://media.giphy.com/media/IYIlvuWc21U4g/source.gif&size=auto 100%
@snap[west span-100]
## @color[firebrick](MATH?!?!)
@snapend
<!-- ![angry](assets/angry-brian-opt.gif) -->
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
---?include=fragments/math-functions.md
---?include=fragments/pure-func.md
---?include=fragments/side-effects.md
---?include=fragments/immutability.md
---?include=fragments/benefits.md
---
# Higher Order functions
+++
@box[bg-orange text-white](In FP, functions are first-class citizens. That is, they are a normal data-type.<br>Therefore, they can be passed as params, assigned to vars, stored in arrays...)
<br><br>
This characteristic of FP languages, grants us the ability to use what the essence of FP is.
+++
@snap[west span-100]
@box[bg-orange text-white](Higher Order functions are just functions that take another function as parameters, return a new function or both.)
<br>
<div class="small fragment">
<p>A math example is the Differentiation</p>
`\[
  \frac{df(x)}{dx}
\]`
<p>that is, a function that takes another function as input and returns its derivative function</p>
</div>
@snapend
+++
@snap[north-west span-100]
#### Higher Order functions example
@snapend
```python
def makeAdder(constantValue):
  def adder(value):
    return constantValue + value

  return adder

add10 = makeAdder(10)
print(add10(20)) # 30
```

`makeAdder` is a higher order function because returns another function.
<p class="fragment">Note that the internal defined function is a CLOSURE</p>
+++
@snap[west list-content-concise span-100]
<p>Properties of higher order functions:</p>
@ul
- Expressive and modular code
- Don't repeat yourself (DRY)
- Loop-less code
@ulend
@snapend
+++
In FP, loop constructs does not exist.<br>They are replaced by special high order functions that guarantee purity and immutability, besides being more expressive.

There exist many of them but they are all just different mixes of two base functions
+++
### Map - Reduce
```python
things = [1,2,3,4]

newThings = map(lambda x: x * 10, things) # [10,20,30,40]
sum = reduce(lambda x, y: x + y, things) # 10
```
@box[bg-orange](Each of these functions let us do common operations on arrays without having to write boilerplate loops)
