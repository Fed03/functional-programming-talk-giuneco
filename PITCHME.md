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
<div class="small">
<p>A math example is the Differentiation</p>
`\[
  \frac{df(x)}{dx}
\]`
<p>that is, a function that takes another function as input and returns its derivative function</p>
</div>
@snapend
