## Functional Programming
### & @color[#f26225](Lambdas)
---
# @color[#f26225](DISCLAIMER)
---?image=template/img/bg/orange.jpg&position=top&size=100% 20%
@snap[north span-100]
@size[1.5em](DISCLAIMER)
@snapend

@ul
- I am no expert in Functional Programming
- There will be a little bit of @color[firebrick](math) concepts
@ulend
---
<!-- ?image=template/img/bg/orange.jpg&position=left&size=35% 100% -->
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
---
# Functions
+++
Math Functions are simple relations between sets: from the @color[#6C8EBF](Domain) to the @color[#B85450](Codomain)
@img[span-60 clean-img](assets/func-diagram.png)
+++
#### Function are mappings between an @color[#6C8EBF](input) and an @color[#B85450](output).

<br>

They can be represented using diagrams
+++
Grahps

<br>

@img[graph-img](assets/func-graph.png)
+++
Or even simple tables


<table class="fragment text-center">
  <tr>
    <th>@color[#6C8EBF](Domain)</th>
    <th>@color[#B85450](Codomain)</th>
  </tr>
  <tr>
    <td>-3</td>
    <td>9</td>
  </tr>
  <tr>
    <td>-2</td>
    <td>4</td>
  </tr>
  <tr>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <td>1</td>
    <td>1</td>
  </tr>
  <tr>
    <td>2</td>
    <td>4</td>
  </tr>
  <tr>
    <td>3</td>
    <td>9</td>
  </tr>
</table>
+++
This tabular idea would allow us to write functions (programming ones) as simple Dictionaries
<br>
```python
pow2 = {
  -3: 9,
  -2: 4,
  0: 0,
  1: 1,
  2: 4,
  3: 9
}

print(pow2[-2])
# 4
```
+++
Naturally functions written like this are not very useful

<br>

We need something more powerful to represent them
+++
## Formulae!

<br>

`\[
  f(x) = \sum_{i=1}^{n} \int_{0}^{\sum_{k=1}^{p} \delta x} \frac{1}{x} dx
\]`
+++?image=assets/jack-sparrow.jpg&size=cover
@snap[west]
## @color[#f26225](WUT?)
@snapend
---
## Let's get @color[#4487f2](Pure)
+++
The foundations of FP are the so called @color[#4487f2](pure) functions.
<br><br><br>
A function is @color[#4487f2](pure) if it follows some policies that make it closely related to the concept of math functions.
+++
@snap[north-west]
@color[#4487f2](Pure) Function Policies
@snapend

@snap[west list-content-concise span-100]
@ol
- Works only with its input (no access to outer context)
- Must have at least 1 param (0-arity not allowed)
- Must return an output
- Without side-effects
@olend
@snapend
+++
@snap[north]
### Pure functions are @color[#f26225](deterministic)
@snapend

@box[bg-orange text-white rounded](Given points 1,2,3,4, all pure functions will always produce the same output when called with the same inputs)
+++
#### Determinism is what makes @color[#4487f2](pure) functions equivalent to the math ones

<br>

This equivalence will allow us to use powerful math tool when structuring our softwares.
---
## @color[#9e35de](Side)-effects
+++
#### @color[#9e35de](Side)-effects represent the interactions with the world outside the function
+++
@snap[north-west]
@color[#9e35de](Side)-effects include but are not limited to
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
#### So, at this point you think...
+++?image=assets/doc-brown.jpg&size=cover
@snap[north-west span-35]
@quote[How the hell am I supposed to do anything useful with only pure functions?!?]
@snapend
+++?image=template/img/bg/white.jpg&position=left&size=38% 100%
@snap[east split-screen-text text-white]
#### FP is not only pure functions
@ul[split-screen-list](false)
- All useful SW has to interact with the outside world
- Try to confine side-effects
- Segregate impure code from pure
- Minimize the amount of impure code
@ulend
@snapend

@snap[west split-screen-fa]
@box[bg-orange text-white rounded](@fa[puzzle-piece fa-5x])
@snapend
