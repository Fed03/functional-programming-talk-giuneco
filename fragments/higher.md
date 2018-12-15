# Higher @color[#4caf50](Order) functions
+++
@box[bg-orange text-white](In FP, functions are first-class citizens. That is, they are a normal data-type.<br>Therefore, they can be passed as params, assigned to vars, stored in arrays...)
<br><br>
This characteristic of FP languages, grants us the ability to use what the essence of FP is.
+++
@snap[west span-100]
@box[bg-orange text-white](Higher Order functions are just functions that take another function as parameters, return a new function or both.)
<br>
<div class="small fragment">
<p>A math example is the Differentiation</p>
`\[
  \frac{df(x)}{dx}
\]`
<p>that is, a function that takes another function as input and returns its derivative function</p>
</div>
@snapend
+++
@snap[north-west span-100]
#### Higher Order functions example
@snapend
```python
def makeAdder(constantValue):
  def adder(value):
    return constantValue + value

  return adder

add10 = makeAdder(10)
print(add10(20)) # 30
```

`makeAdder` is a higher order function because it returns another function.
<p class="fragment">Note that the internal defined function is a CLOSURE</p>
+++
@snap[north-west span-100]
#### Properties of higher order functions:
@snapend
@snap[west list-content-concise span-100]
@ul
- Expressive and modular code
- Don't repeat yourself (DRY)
- Loop-less code
@ulend
@snapend
+++
In FP, loop constructs do not exist.<br><br>

They are replaced by special higher order functions that guarantee purity and immutability, besides being more expressive.<br><br>

Many of them exist, but they are all just different mixes of two base functions.
+++?image=assets/bg/orange.jpg&position=top&size=100% 16%
@snap[north span-100]
### Map & Reduce
@snapend

```python
things = [1,2,3,4]

newThings = map(lambda x: x * 10, things) # [10,20,30,40]
sum = reduce(lambda x, y: x + y, things, 0) # 10
```

Each of these functions let us do common operations on arrays without having to write boilerplate loops
