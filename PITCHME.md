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
---?include=fragments/math-functions.md
---?include=fragments/pure-func.md
---?include=fragments/side-effects.md
---?include=fragments/immutability.md
---
# Benefits?
+++
@snap[north-west]
#### Benefits
@snapend
@snap[west]
At this point you may ask why anyone would want to "relearn" how to code and with all of this constraints
@snapend
+++
@snap[north-west]
Using @color[#4487f2](pure) functions and following the @color[mediumaquamarine](immutability) priciples has many benefits
@snapend
@snap[west list-content-concise]
@ol
- PF are self-documenting (must declare their deps)
- They are testable
- They are cacheable (due to their deterministic nature)
- They are reasonable
  @ul[list-content-concise fragment](false)
  - Knowing that they do not depend on anything external, decreases the cognitive load
  - Referential transparency
  @ulend
- Thanks to immutability, PF are inherently thread-safe (parallelize all the things!)
@olend
@snapend
