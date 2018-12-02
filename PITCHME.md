## Functional Programming
### & @color[#f37b21](Lambdas)
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
# @color[#f37b21](DISCLAIMER)
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
- @color[#f37b21](Lambda) calculus
@ulend
@snapend
---?include=fragments/math-functions.md
---?include=fragments/pure-func.md
---?include=fragments/side-effects.md
---?include=fragments/immutability.md
---?include=fragments/benefits.md
---
@img[clean-img lambda](assets/lambda-logo.png)
### @color[#f37b21](Lambdas)
+++
@snap[north-west span-100]
#### `\(\lambda\)` Calculus 101
@snapend
@quote[Lambda calculus is a formal system in math logic for expressing computation based on function abstraction using variable binding and substitution. It is a universal model of computation that can be used to simulate any Turing machine.](Wikipedia)
+++
@snap[north-west span-100]
#### `\(\lambda\)` Calculus 101
@snapend

`\[
  \lambda x.E
\]`

This is a @color[#f37b21](lambda) abstraction, where `\(E\)` is an expression and `\(x\)` is a variable.

The following lambda term

`\[
  (\lambda x.\ + x\quad5)\ 3
\]`

means that `\(x\)` is bound to `\(3\)`, so we replace any occurence of `\(x\)` inside the expression with `\(3\)`. After we can evaluate the expression body with a result of `\(8\)`.
+++
@snap[north-west span-100]
#### `\(\lambda\)` Calculus 101
@snapend
@color[#f37b21](`\(\lambda\)`) calculus, therefore, resembles a function definition, where `\(E\)` is the function body and `\(\lambda x.\)` its parameter.
---?include=fragments/higher.md
