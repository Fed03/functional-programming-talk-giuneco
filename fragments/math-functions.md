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
Obviously functions written like this are not very useful

<br>

We need something more powerful to represent them
+++
## Formulae!
<br>
`\[
  f(x) = \sum_{i=1}^{n} \int_{0}^{\sum_{k=1}^{p} \delta x} \frac{1}{x} dx
\]`
+++?image=assets/jack-sparrow.png&size=cover
@snap[west]
## @color[#f26225](WUT?)
@snapend
