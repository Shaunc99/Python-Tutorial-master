
import json
from Class import Animal

animal1 = Animal("lion1", "Land", "Warm-blooded", 6)
animal2 = Animal("lion2", "Land", "Warm-blooded", 7)
animal3 = Animal("lion3", "Land", "Warm-blooded", 8)
animal4 = Animal("lion4", "Land", "Warm-blooded", 6)
animal5 = Animal("lion5", "Land", "Warm-blooded", 6)
animal7 = Animal("lion6", "Land", "Warm-blooded", 6)
animal8 = Animal("lion7", "Land", "Warm-blooded", 6)
animal9 = Animal("lion8", "Land", "Warm-blooded", 6)

animal_list = [animal1,animal2,animal3,animal4,animal5,animal7]

for x in animal_list:
    print(x.name + " is " + str(x.age) + " years old")


list_names=["shsyan","rizwan", "emaan", "khalidah"]
print (*list_names)