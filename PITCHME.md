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
---?include=fragments/lambda.md
---?include=fragments/higher.md
---
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

filterCur(hasLetterR, ['rock', 'jazz']) # ['rock and roll']

removeStringsWithoutRs = filterCur(hasLetterR)
removeStringsWithoutRs(['rock', 'jazz', 'rnb']) # ['rock', 'rnb']

noVowels = replaceCur('[aeiou]')
censored = noVowels('*')
censored('Chocolate Rain') # 'Ch*c*l*t* R**n'
```
@[1-3](Curryed versions of standard funcs)
@[5, 11](When called with all the expected args, it behaves like the standard func)
@[7-9,13-14](Create new specialized function and reuse it)
@[16-18](Preload arguments more than once)
<br><br>