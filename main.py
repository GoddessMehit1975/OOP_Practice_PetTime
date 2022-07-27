class Pet:
    def __init__(self):
        self.name = input("What is your pet's name?").lower()
        self.age = input("How old is your pet?").lower()
        self.color = input("What is your pet's color?").lower()

    def displaypet(self):
        self.breed = input("What type is your pet? (Dog, Cat, ...)").lower()
        print("My pet's name is", self.name, "\n"
              "They are", self.color, "\n"
              "They are", self.age,
              "years old")
        if self.breed == "Dog":
            print("Bark Bark")
        elif self.breed == "Cat":
            print("Meow Meow")
        elif self.breed == "Fish":
            print("Glub Glub")
        else:
            print("You own an alien")

    def dogspeak(self):
        print("Bark Bark")

    def catspeak(self):
        print("Meow Meow")

    def fishspeak(self):
        print("Glub Glub")


pet1 = Pet()
print("")
# pet2 = Pet()
# print("")
# pet3 = Pet()
# print("")
# pet4 = Pet()
print("")
pet1.displaypet()
# print("")
# pet2.displaypet()
# print("")
# pet3.displaypet()
# print("")
# pet4.displaypet()
# print("")
