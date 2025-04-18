import random
import math

class Drone:
    def __init__(self):
        self.x = 0
        self.y = 0

    def move(self):
        """Randomly move the drone one step N, S, E, or W"""
        direction = random.choice(['N', 'S', 'E', 'W'])
        if direction == 'N':
            self.y += 1
        elif direction == 'S':
            self.y -= 1
        elif direction == 'E':
            self.x += 1
        elif direction == 'W':
            self.x -= 1

    def get_distance(self):
        """Return the Euclidean distance from the start"""
        return math.sqrt(self.x**2 + self.y**2)

    def reset(self):
        """Reset the drone to the origin"""
        self.x = 0
        self.y = 0

# --- Test run ---
drone = Drone()
steps = 10
for i in range(steps):
    drone.move()

print(f"After {steps} steps, drone is {drone.get_distance():.2f} units from start.")
