### Introduction to
## @color[#f26225](Functional) Programming
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
---?include=fragments/lambda.md
---?include=fragments/higher.md
---?include=fragments/curry.md
---
# @color[#e53935](Compose) all the things
+++
@snap[north-west span-100]
#### @color[#e53935](Composing)
@snapend
Code reuse sounds great but is difficult to achieve.

Make the code too specific and it can't be reused.<br>
Make it too general and it can be difficult to use it in the first place.
+++
@snap[north-west span-100]
#### @color[#e53935](Composing)
@snapend
In math, function composition is the application of one function to the result of another to produce a third function.

Given the functions `\(f: A \mapsto B\)` and `\(h: B \mapsto C\)`, we can compose them into a new function `\((\ h \circ f\ ): A \mapsto C\)` defined as

`\[
  (\ h \circ f\ )(x) = h(\ f(x)\ )
\]`
+++
@snap[north-west span-100]
#### @color[#e53935](Composing)
@snapend
That same thing is possible in code
```python
compose = lambda h, f: lambda x: h(f(x))

mult4 = lambda x: x * 4
add30 = lambda x: x + 30

answer = compose(add30, mult4)

print(answer(3)) # 42
```
@[1](Simple version of compose function)
@[3-6](Composing two functions to find...)
@[8](...the answer!)
<br>
+++
@snap[north-west span-100]
#### @color[#e53935](Compose) characteristics
@snapend
@snap[west small span-100]
<p>In `(( h circ f ))` the first applied function is the rightmost; `compose` respects this creating a right to left data flow.</p>
<div class="fragment">
<p>Composition is *associative* meaning that</p>
`[
  ( h circ ( g circ f ) ) = ( ( h circ g ) circ f ) = ( h circ g circ f )
]`
</div>
@snapend
+++
@snap[north-west span-100]
#### @color[#e53935](Compose) characteristics
@snapend
Associativity provides the ability to be more concise or more expressive depending on the situation
+++
<p class="fragment">Since the outer function must receive as input the output of the inner one, these two must be compatible. Aside from Type, code functions returns just 1 thing but they can have multiple inputs.</p>
