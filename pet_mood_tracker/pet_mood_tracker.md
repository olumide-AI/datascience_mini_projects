# 📁 week1_pet_mood_tracker

# README.md

## 🐶 Project: Pet Mood Tracker

### 🧠 Goal

Create a simple `Pet` class that stores your pet’s name and tracks its mood over a week. You’ll simulate mood changes, store them in a list, and plot them using `matplotlib`.

### 🔧 Tools You’ll Practice

- Python classes (`__init__`, attributes, methods)
- Lists and loops
- Matplotlib line plots
- GitHub commit flow

---

## 📚 Learning Plan (Guided + Beginner Friendly)

### 📘 Part 1: Understanding Classes in Python

Before you write any code:

- 📺 [Corey Schafer: Python OOP Tutorial - Classes and Instances](https://www.youtube.com/watch?v=ZDa-Z5JzLYM&t=128s)
  - Watch until the end of the `__init__` and instance methods explanation (~10 min)
- ✅ When ready: Try creating your `Pet` class in `pet.py` with `name` and `mood` attributes

💡 **Check-in Questions:**

- What is `self`? Why do we use it?
- Can you explain what `__init__` does in your own words?
- What does your class store or track

**Answer to check-in question:**

- ✅ You’re close — self is how the class refers to itself.
It's used to access or update that object’s data from inside its own methods.
It’s not just a Python rule — it gives each object its own identity.
- __init__() is the constructor. It’s automatically called when you create an object.
You use it to set up the initial state of each object.
- My class stores mood and the pet name at this present time 

📝 **Git Commit:**

```bash
git add pet.py
git commit -m "Create Pet class with mood tracking"
```

---

### 📘 Part 2: Using Loops and Lists

Now, simulate 7 days of mood changes.

- 📄 [W3Schools - Python For Loops](https://www.w3schools.com/python/python_for_loops.asp)
- 📄 [W3Schools - Python Lists](https://www.w3schools.com/python/python_lists.asp)

💡 **Tasks:**

- Write a `change_mood()` method in your `Pet` class that randomly adjusts the mood (+1 or -1)
- In `main.py`, create a loop that simulates 7 days and stores mood values in a list

📝 **Git Commit:**

```bash
git add main.py
git commit -m "Simulate 7 days of mood changes"
```

---

### 📘 Part 3: Plotting With Matplotlib

Time to visualize!

- 📺 [Matplotlib Beginner Tutorial - Creating Line Graphs](https://www.youtube.com/watch?v=DAQNHzOcO5A)
  - Watch until the part where a basic line plot is shown (~7–10 mins)

💡 **Tasks:**

- Import `matplotlib.pyplot`
- Plot mood values over 7 days (x = Day 1 to 7, y = mood)

📝 **Git Commit:**

```bash
git add main.py
```

git commit -m "Add matplotlib line plot for mood values"

```

---

### 🧠 Bonus Challenge
- Add `feed()` and `play()` methods
- Use user input to simulate which activity happens each day
- Cap mood values between 0 and 10

📄 [Real Python - Python Input() Function](https://realpython.com/python-input-function/)

📝 **Git Commit:**
```bash
git commit -m "Add bonus methods: feed and play"
```

---

## 🗂️ File Structure Suggestion

```
week1_pet_mood_tracker/
├── pet.py         # your class goes here
├── main.py        # the script that runs the simulation
└── README.md      # this file with instructions
```

---

## 💻 GitHub Setup (Recap)

```bash
git init
git add .
git commit -m "Initial setup: Pet Mood Tracker template"
git branch -M main
git remote add origin <your-repo-url>
git push -u origin main
```

Commit often. Think of each commit as a checkpoint in your learning journey.

When done, reflect:
> What was hard? What surprised you? What do you feel proud of?

Then tell me, and I’ll check if you’ve unlocked a **level-up badge** 🏅
