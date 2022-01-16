# // print_each_character_with_space("rizwan") r i z w a n



def print_characters(text):
    for i in range(0, len(text)):
        print(i, text[i])

# print_vowels(text)

def print_vowels(words):
    print("The word is", words, ".")
    for i in range(0, len(words)):
        ia = words[i]
        if ia == "a" or ia == "e" or ia == "i" or ia == "o" or ia == "u":
            print("A vowel is found!!", ia, "at letter", i + 1)
        else:
            pass

# print_vowels("bye")

# print_fancy_letters("shayan") sHaYaN

def print_fancy_letters(letters):

    for i in range(0, len(letters)):
        if i %2 == 0:
            print(letters[i].upper(), end="")
        else:
            print(letters[i].lower(), end="")


# print_fancy_letters("Khalida Rizwan")


def print_fancy_vowels(words):
    for i in range(0, len(words)):
        a = words[i]
        if a == "a" or a == "e" or a == "i" or a == "o" or a == "u":
            print(words[i].upper(), end="")
        else:
            print(words[i].lower(), end="")


print_fancy_vowels("This is a nice, lovely, and scrumptious cake.")
