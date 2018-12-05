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
<div class="align-left">
  <p>In `\((\ h \circ f\ )\)` the first applied function is the rightmost; `compose` respects this creating a right to left data flow.</p>
  <br>
  <div class="fragment">
    <p>Composition is *associative* meaning that</p>
    `\[
      h \circ (\ g \circ f\ ) = (\ h \circ g\ ) \circ f = h \circ g \circ f
    \]`
  </div>
</div>
+++
@snap[north-west span-100]
#### @color[#e53935](Compose) characteristics
@snapend
Associativity provides the ability to be more concise or more expressive depending on the situation
```python
# Given a strings array
lastElementUpperVowels = compose(vowels, toUpperCase, first, reverse)

lastElement = compose(first, reverse)
lastElementUpperVowels = compose(toUpperCase, vowels, lastElement)

lastElement = compose(first, reverse)
upperVowels = compose(toUpperCase, vowels)
lastElementUpperVowels = compose(upperVowels, lastElement)
```
@[1-2](Like this)
@[1,4-5](or this)
@[1,7-9](or even this)
+++
@snap[north-west span-100]
#### @color[#e53935](Compose) characteristics
@snapend
Since the outer function must receive as input the output of the inner one, these two must be compatible.

Aside from *type*, code functions return just 1 thing but they can have multiple inputs.
+++
@box[bg-orange normal-text](In order to compose functions, they should be called with only one parameter.<br><br>Here currying comes to save the world. Proper lambdas works well, too.)
+++?image=assets/lego.png&size=contain&color=black
@box[bg-semi h2](Thanks to currying,<br>pure functions are composable like<br>LEGO blocks!)