#!/usr/bin/env python3

class Dog:
    pass
    def __init__(self,name,breed = "Mutt"):
        self.name = name
        self.breed = breed
        
    
champ = Dog("champ")
print (champ.name)
print(champ.breed)