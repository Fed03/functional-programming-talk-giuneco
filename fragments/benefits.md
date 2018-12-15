# Benefits?
+++
@snap[north-west]
## Benefits
@snapend
@snap[west]
At this point you may ask, why would anyone want to "relearn" how to code?<br>With all of these constraints too!
@snapend
+++
@snap[north-west]
Using @color[#4487f2](pure) functions and following the @color[#1dc579](immutability) principles has many benefits
@snapend
@snap[west list-content-concise span-100]
@ol
- Pure functions are self-documenting (must declare their dependencies)
- They are testable
- They are cacheable (due to their deterministic nature)
@olend
@snapend
+++
@snap[west list-content-concise span-100]
@ol[continue-list from-4]
- Thanks to immutability, pure functions are inherently thread-safe (parallelize all the things!)
- They are reasonable
  @ul[list-content-concise fragment](false)
  - Knowing that they do not depend on anything external decreases the cognitive load
  - Referential transparency
  @ulend
@olend
@snapend
+++?image=assets/bg/orange.jpg&position=top&size=100% 16%
@snap[north span-100]
### Referential transparency
@snapend
@snap[west]
Referential Transparency is a fancy term to describe that a pure function can be safely replaced by its expression.
@snapend
+++
@snap[north-west span-100]
#### @color[#f26225](Referential transparency)
@snapend
```python
sylvanas = {"name": "sylvanas", "hp": 10, "team": "horde"}
malfurion = {"name": "malfurion", "hp": 10, "team": "alliance"}

def decrementHp(npc):
  updatedNpc = npc.copy()
  updatedNpc["hp"] -= 1
  return updatedNpc

def isSameTeam(npc1,npc2):
  return npc1["team"] == npc2["team"]

def punch(attacker,target):
  return target if isSameTeam(attacker,target) else decrementHp(target)

punch(sylvanas, malfurion)
# {'name': 'malfurion', 'hp': 9, 'team': 'alliance'}
```
@[4-13](Pure functions)
@[15-16](This call is simple to debug)
+++
<p class="align-left small">Using pure functions we can substitute them "equals for equals" to reason about the code.<br>It's like manually evaluating code!</p>
```python
def punch(attacker,target):
  return target if attacker["team"] == target["team"] else decrementHp(target)

def punch(attacker,target):
  return target if "horde" == "alliance" else decrementHp(target)

def punch(attacker,target):
  return decrementHp(target)

def punch(attacker,target):
  updatedNpc = npc.copy()
  updatedNpc["hp"] -= 1
  return updatedNpc
```
@[1-2](1. Inline the function `isSameTeam`)
@[4-5](2. Data is immutable. Sobstitute with actual values)
@[7-8](3. The condition is false. Remove the branch)
@[10-13](4. Inline the function `decrementHp`)
<br><br>
+++?image=assets/bg/orange.jpg&position=top&size=100% 16%
@snap[north span-100]
### Referential transparency
@snapend
@snap[west span-100]
This property is exceptional for refactoring and understanding code.
<br>
In fact, we use this technique everyday to refactor someone else's code.
@snapend
