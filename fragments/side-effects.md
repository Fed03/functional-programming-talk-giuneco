# @color[#9e35de](Side)-effects
+++
#### @color[#9e35de](Side)-effects represent the interactions with the world outside the function
+++
@snap[north-west]
@color[#9e35de](Side)-effects include, but are not limited to:
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
#### So, at this point you're thinking...
+++?image=assets/doc-brown.jpg&size=cover
@snap[north-west span-35]
@quote[How the hell am I supposed to do anything useful with only pure functions?!?]
@snapend
+++?image=assets/bg/white.jpg&position=left&size=50% 100%
@snap[east split-screen-text text-white]
#### @color[#f26225](FP) is not only pure functions
@ul[split-screen-list](false)
- All useful SW has to interact with the outside world
- Try to confine @color[#9e35de](side)-effects
- Segregate impure code from @color[#4487f2](pure)
- Minimize the amount of impure code
@ulend
@snapend

@snap[west split-screen-fa]
@box[bg-orange text-white rounded](@fa[puzzle-piece fa-5x])
@snapend
