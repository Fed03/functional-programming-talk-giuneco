@img[clean-img lambda](assets/lambda-logo-2.png)
### @color[#f26225](Lambdas)
+++?image=assets/half-life.png&position=bottom&size=100% auto
@snap[north-west span-100]
#### `\(\lambda\)` Calculus 101
@snapend
<div class="small">
@quote[Lambda calculus is a formal system in math logic for expressing computation based on function abstraction using variable binding and substitution. It is a universal model of computation that can be used to simulate any Turing machine.](Wikipedia)
</div>

`\[
  \lambda x.E
\]`

This is a lambda abstraction, where `\(E\)` is an expression and `\(x\)` is a variable.
+++?image=assets/bg/orange.jpg&position=top&size=100% 14%
@snap[north-west span-100]
#### `\(\lambda\)` Calculus 101
@snapend
@snap[center span-100]
<p>The following lambda term</p>

`\[
  (\lambda x.\ +\ x\ 5)\ 3
\]`

<p>means that `\(x\)` is bound to `\(3\)`, so any occurrence of `\(x\)` inside the expression can be replaced with `\(3\)`. Therefore, the expression body can be evaluated with a result of `\(8\)`.</p>
@snapend
+++?image=assets/bg/orange.jpg&position=top&size=100% 14%
@snap[north-west span-100]
#### `\(\lambda\)` Calculus 101
@snapend
@snap[center span-100]
<p>`\(\lambda\)` term, therefore, resembles a function definition without name, where `\(E\)` is the function body and `\(\lambda x.\)` its parameter.</p>
<p class="fragment">Note that lambda terms must have exactly 1 parameter</p>
@snapend
+++
Going back to programming, @color[#f26225](lambdas) are simply expressions whose value is a function.

They are often called anonymous functions, although this definition is not completely right.
@ul[fragment](false)
- Typically one lined
- Often 1 parameter, rarely 2, never more
- Small
- Pure
- Disposable
@ulend
+++
@snap[north span-100]
#### Examples
@snapend
C#
```C#
Function<string, int> Length = (str) => str.Length
```

Javascript
```javascript
var Length = (str) => str.length
```

Python
```python
length = lambda str: len(str)
```
