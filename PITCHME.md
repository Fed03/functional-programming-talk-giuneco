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
@img[clean-img lambda](assets/lambda-logo-2.png)
### @color[#f26225](Lambdas)
+++?image=assets/half-life.jpg&size=contain
@snap[north-west span-100]
#### `\(\lambda\)` Calculus 101
@snapend
<div class="small">
@quote[Lambda calculus is a formal system in math logic for expressing computation based on function abstraction using variable binding and substitution. It is a universal model of computation that can be used to simulate any Turing machine.](Wikipedia)
</div>

`\[
  \lambda x.E
\]`

This is a lambda @color[#f26225](abstraction) , where `\(E\)` is an expression and `\(x\)` is a variable.
+++?image=assets/bg/orange.jpg&position=top&size=100% 16%
@snap[north-west span-100]
#### `\(\lambda\)` Calculus 101
@snapend
The following lambda term

`\[
  (\lambda x.\ +\ x\ 5)\ 3
\]`

means that `\(x\)` is bound to `\(3\)`, so any occurrence of `\(x\)` inside the expression can be replaced with `\(3\)`. Therefore, the expression body can be evaluated with a result of `\(8\)`.
+++?image=assets/bg/orange.jpg&position=top&size=100% 16%
@snap[north-west span-100]
#### `\(\lambda\)` Calculus 101
@snapend
`\(\lambda\)` calculus, therefore, resembles a function definition, where `\(E\)` is the function body and `\(\lambda x.\)` its parameter.
---?include=fragments/higher.md
