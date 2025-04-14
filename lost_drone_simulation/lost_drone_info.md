# Project

## Phase 1: Core Setup (Today’s focus)

- Let’s build just enough to:
- Create a Drone class
- Move the drone randomly N/S/E/W
- Return the drone’s final position after N steps
- We’ll expand this into data analysis + plots next.

## What this reinforces

- Classes and methods in Python
- Loops and conditionals
- Randomness
- Basic math (Pythagorean distance)

## Your Tasks

- Run this code (in VS Code or a terminal)
- Change steps to 50, 100, 1000 — how does the distance change?
- Write down:
  - What happens when you run it?
  - What do you think is happening behind the scenes?
  - What questions pop into your head?

## Study Tools (ONLY what helps right now)

1. Corey Schafer - Python OOP (15 mins):

- If you’re new to classes and methods in Python: 🔗 Corey Schafer - Python OOP Tutorial 1
- Watch only until the __init__ and instance method part.
- Then come back and re-read the Drone class above — you’ll notice more!

2. Practice prompt (LeetCode-style logic):

- Modify the simulation:
- Add a counter: how many times did the drone step North?
- What’s the final (x, y) position?
- Example: print(f"Final position: ({drone.x}, {drone.y})")

3. Phase 2: Simulate the drone 1000 times and store the distances and Phase 3: Plot the distribution with matplotlib
