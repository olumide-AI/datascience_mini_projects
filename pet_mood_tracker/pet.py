class Pet:
    def __init__(self, name, mood):
        # Start your attributes here
        self.name = name
        self.mood = mood
        

    def change_mood(self):
        # This method will be used later
        pass

pet_buddy = Pet("Buddy","happy")
print(pet_buddy)