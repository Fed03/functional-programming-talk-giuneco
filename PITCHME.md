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


They can be represented using diagrams
+++
Grahps


@img[fragment graph-img](assets/func-graph.png)
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


We need something more powerful to represent them
+++
`\[
  f(x) = \sum_{i=1}^{n} \int_{0}^{\sum_{k=1}^{p} \delta x} \frac{1}{x} dx
\]`
