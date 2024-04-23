class Animal :
    def __init__(self, type, name, gender, likes, dislikes) :
        self.animal = type
        self.name = name
        self.gender = gender
        self.likes = likes
        self.dislikes = dislikes

list_step = 0
animal = []
zoo_list = []

def create_animal() :
    global list_step
    name = input(print("What is the name of the animal?:"))
    type = input(print("What type of animal is", name + "?:"))
    gender = input(print("What gender is", name + "?:"))
    likes = input(print("What does the", name + "like?:"))
    dislikes = input(print("what does", name + "dislike?:"))

    animal[list_step] = Animal(type, name, gender, likes, dislikes)

    zoo_list[list_step] = animal[list_step]

    list_step = list_step + 1

create_animal()

print(zoo_list[0])

