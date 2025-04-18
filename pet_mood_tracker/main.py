from pet import Pet

pet_buddy = Pet("Buddy", 5)
moods = []
for day in range(7):
    pet_buddy.change_mood()
    moods.append(pet_buddy.mood)

print(f"{pet_buddy.name}'s mood over the week: {moods}")