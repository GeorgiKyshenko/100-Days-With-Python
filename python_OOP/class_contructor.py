class Animal:
    def __init__(self, animal_type, speed, family):
        self.animal_type = animal_type
        self.speed = speed
        self.family = family


animal_1 = Animal("Tiger", 30, "Cats")
animal_2 = Animal("Eagle", 60, "Birds")

print(f"Animal 1 - Type: {animal_1.animal_type}, Speed: {animal_1.speed}, Family: {animal_1.family}")
print(f"Animal 2 - Type: {animal_2.animal_type}, Speed: {animal_2.speed}, Family: {animal_2.family}")

