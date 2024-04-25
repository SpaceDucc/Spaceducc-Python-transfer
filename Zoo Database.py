class Animal :
    def __init__(self, name, type, gender, likes, dislikes) :
        self.name = name
        self.animal = type
        self.gender = gender
        self.likes = likes
        self.dislikes = dislikes

    def printinfo(self) :
        print("This animal's name is", self.name + ".")
        print(self.name, " is a", self.animal + ".")
        print(self.name, "is", self.gender + ".")
        print(self.name, "likes", self.likes + ".")
        print(self.name, "dislikes", self.dislikes + ".")


list_step = int(0)
animal = []
zoo_list = []
fakevar2 = 1

def create_animal() :
    global list_step
    fakevar4 = 1
    x = 1
    while x == 1 :
        name = input("What is the name of the animal?:")
        type = input("What type of animal is " + name + "?:")
        gender = input("What gender is " + name + "?:")
        likes = input("What does the " + name + " like?:")
        dislikes = input("what does " + name + " dislike?:")

        animal.append(Animal(name, type, gender, likes, dislikes))

        zoo_list.append(animal[list_step])

        list_step = list_step + 1
        while fakevar4 == 1 :
            try :
                x = int(input("Would you like to make another animal?(1 for yes, 0 for no)"))
            except ValueError :
                pass
            if x != 1 and x != 0 :
                print("that is not 1 or 0")
            else :
                pass
            

def search_animals() :
    global zoo_list
    fakevar3 = 1
    length = len(zoo_list)

    for i in range(length) :
        print(zoo_list[i].name, "is", i, "on the list.")

    while fakevar3 == 1 :
        search_term = int(input("What is the number of the animal you want to look up?"))

        try :
            zoo_list[search_term].printinfo()
        except IndexError :
            print("That is not a valid search term")
        else :
            fakevar3 = 0


def what_command() :
    global fakevar2 
    command = input("What would you like to do?(type create to create some animals, type search to look at your animals, type quit to quit):")
    fakevar1 = 1
    while fakevar1 == 1 :
        if command.lower() == "create" :
            create_animal()
            fakevar1 = 0
        elif command.lower() == "search" :
            search_animals()
            fakevar1 = 0
        elif command.lower() == "quit" :
            fakevar2 = 0
            fakevar1 =0
        else :
            print("invalid command")
            command = input("What would you like to do?(type create to create some animals, type search to look at your animals, type quit to quit):")
    
def run_zoo() :
    global fakevar2
    create_animal()
    while fakevar2 == 1 :
        what_command()


run_zoo()