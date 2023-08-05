# OOTUI
## Object-Oriented Terminal User Interface

---
# Alpha state

the package does not yet live up to some details given in the readme

---
OOTUI is a package for creating easy to read data displays in your terminal. <sub>(or games if you're crazy like that)</sub>

you create displays by creating objects that hold the data that you want to display (and updating these objects whenever necessary). You decorate or divide this data by creating more objects (like BorderRects).

Each object has a position and a size, so any object can appear anywhere on the terminal

## Parent-Child structure
Any drawable(a OOTUI object that 'draws' on the terminal) can have a parent and any number of children.

When a drawable 'updates'(redraw its portion of the terminal) all of its will update as well before its portion is redrawn.

a child can overwrite (part of) its parent, meaning that, for example: you can layer multiple line-graphs over each other.

The position of a drawable is relative to its parent (and optionally its size as well), this means that groups of objects automatically stick together

## Use Window to take over the entire terminal... or don't.
Any drawable can output itself and the sum of its children at any time with a normal print statement. This is for if you just want to show a graph or two every once in a while.

If you use the window object, you overwrite the whole terminal, and can position your drawables anywhere on this terminal. You can update this window as often as you'd like to get real-time data from multiple drawables at once.

A window knows the size of your terminal, so your drawables can reposition and rescale itself, based on this size (optionally in real time)

You can use multiple windows to switch between structures of drawables, fast. (you can think of these as different screens)

## efficient
Even very complex structures of drawables (with many children (both in depth (grandchildren) and in width (siblings))) can usually be updated and drawn within a tenth of a second.

If that isn't enough, you don't need to update every drawable every 'frame', you can just update the drawables that you want to update, and they will cascade their part of the terminal back to the root object