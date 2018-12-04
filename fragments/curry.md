# Spice it up with @color[#a77f0e](currying)
+++
The concept of currying is simple: call a function with less arguments that it expects, and return a new function that takes the remaining ones.

The makeAdder function we've just seen is an example of currying:
```python
def makeAdder(constantValue):
  return lambda value: constantValue + value

add10 = makeAdder(10)
increment = makeAdder(1)

increment(3) # 4
add10(32) # 42
```
+++
Luckily, there is a function named `curry` that enables this behavior for any common defined function
```python
add = curry(lambda x, y: x + y)

add10 = makeAdder(10)
increment = makeAdder(1)

increment(3) # 4
add10(32) # 42
```
+++
```python
containsCur = curry(lambda search, string: search in string)
filterCur = curry(lambda fn, iterable: filter(fn, iterable))
replaceCur = curry(lambda search, new, string: re.sub(search, new, string))

containsCur('r', 'hello world') # true

hasLetterR = containsCur('r')
hasLetterR('hello world') # true
hasLetterR('just j and s and t etc') # false

filterCur(hasLetterR, ['rock', 'jazz']) # ['rock']

removeStringsWithoutRs = filterCur(hasLetterR)
removeStringsWithoutRs(['rock', 'jazz', 'rnb']) # ['rock', 'rnb']

noVowels = replaceCur('[aeiou]')
censored = noVowels('*')
censored('Chocolate Rain') # 'Ch*c*l*t* R**n'
```
@[1-3](Curryed versions of base funcs)
@[5, 11](When called with all the expected args, it behaves like the base func)
@[7-9,13-14](Create new specialized functions and reuse them)
@[16-18](Preload arguments more than once)
<br><br>
+++
@snap[north-west span-100]
#### @color[#a77f0e](Currying)
@snapend
<div class="small">
New functions can be created just by giving to base functions some arguments.

Moreover any function that works on single elements can be transformed into a function that works on arrays simply by wrapping it with the curryed version of map:
</div>
```python
mapCur = curry(lambda fn, array: map(fn, array))

getChildren = lambda x: x.childNodes
allTheChildren = map(getChildren)
```
+++
@snap[north-west span-100]
#### @color[#a77f0e](Currying)
@snapend
We said that @color[#4487f2](pure) functions should be called with exactly 1 argument.<br>

Currying does exactly this: each single argument returns a new function expecting the remaining arguments.
