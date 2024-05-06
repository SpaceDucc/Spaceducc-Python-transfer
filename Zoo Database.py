class Animal :
    def __init__(self, name, type, gender, likes, dislikes, how_often_feed) :
        self.name = name
        self.type = type
        self.gender = gender
        self.likes = likes
        self.dislikes = dislikes
        self.feed = how_often_feed

    def printinfo(self) :
        pass

class Bird(Animal) :
    def __init__(self, name, type, gender, likes, dislikes, how_often_feed, wingspan) :
        self.wingspan = wingspan
        Animal().__init__(self, name, type, gender, likes, dislikes, how_often_feed)
        
    def printinfo(self) :
        print("This animal's name is", self.name + ".")
        print(self.name, " is a", self.type + ".")
        print(self.name, "is", self.gender + ".")
        print(self.name, "likes", self.likes + ".")
        print(self.name, "dislikes", self.dislikes + ".")
        print(self.name, "has to be fed every", self.feed, "hours.")
        print(self.name, "eats seeds and bugs.")
        print(self.name, "has a wingspan of", self.wingspan, "inches.")

class Lizard(Animal) :
    def __init__(self, name, type, gender, likes, dislikes, how_often_feed, scale_color) :
        self.color = scale_color
        Animal().__init__(self, name, type, gender, likes, dislikes, how_often_feed)

    def printinfo(self) :
        print("This animal's name is", self.name + ".")
        print(self.name, " is a", self.type + ".")
        print(self.name, "is", self.gender + ".")
        print(self.name, "likes", self.likes + ".")
        print(self.name, "dislikes", self.dislikes + ".")
        print(self.name, "has to be fed every", self.feed, "hours.")
        print(self.name, "eats rodents and bugs.")
        print(self.name, "scales are", self.color + ".")

class Mammal(Animal) :
    def __init__(self, name, type, gender, likes, dislikes, how_often_feed, litter_size) : #add if herbavore or carnivore or omnivore
        self.litter = litter_size
        Animal().__init__(self, name, type, gender, likes, dislikes, how_often_feed)

    def printinfo(self) :
        print("This animal's name is", self.name + ".")
        print(self.name, " is a", self.type + ".")
        print(self.name, "is", self.gender + ".")
        print(self.name, "likes", self.likes + ".")
        print(self.name, "dislikes", self.dislikes + ".")
        print(self.name, "has to be fed every", self.feed, "hours.")
        print(self.name, "eats meat and plants.")
        print(self.type + "'s have an average litter size of", self.litter + ".")

class Fish(Animal) :
    def __init__(self, name, type, gender, likes, dislikes, how_often_feed, prefered_temp) :
        self.temp = prefered_temp
        Animal().__init__(self, name, type, gender, likes, dislikes, how_often_feed)

    def printinfo(self) :
        print("This animal's name is", self.name + ".")
        print(self.name, " is a", self.type + ".")
        print(self.name, "is", self.gender + ".")
        print(self.name, "likes", self.likes + ".")
        print(self.name, "dislikes", self.dislikes + ".")
        print(self.name, "has to be fed every", self.feed, "hours.")
        print(self.name, "eats fish and plants.")
        print(self.name, "prefers a water temp of", self.temp + "°F.")



list_step = int(0)
animal = []
zoo_list = []
fakevar2 = 1

def create_animal() :
    global list_step
    fakevar5 = 1
    fakevar4 = 1
    fakevar6 = 1
    x = 1
    while fakevar5 == 1 :
        while fakevar6 == 1 :
            try :
                what_type = int(input("What type of animal are you making(1 for bird, 2 for lizard, 3 for mammal, 4 for fish)?"))
            except IndexError :
                print("That is not a valid choice")
            else :
                pass
            if what_type > 0 and what_type < 5 :
                fakevar6 = 0
            else :
                

            
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