import random
class Pet:
    def __init__(self, name, mood):
        # Start your attributes here
        self.name = name
        self.mood = mood
        

    def change_mood(self):
        # Change self.mood by either +1 or -1
        # If mood is a number, use random.choice to decide
        # Then update self.mood
        # mood is a number when 1 is low and 10 is higher
        self.mood += random.choice([-1,1])

pet_buddy = Pet("Buddy",5)
print(pet_buddy.change_mood())