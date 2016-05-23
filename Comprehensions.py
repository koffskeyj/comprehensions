sentence = "List comprehensions are the greatest!"


def remove_vowels(b):
    new = b
    vowels = ["a", "e", "i", "o", "u"]
    for a in b.lower():
        if a in vowels:
            new = new.replace(a, "")

    return new


def remove_vowels_comp(b):
    new = b
    vowels = ["a", "e", "i", "o", "u"]
    new = [new.replace(a, "") for a in b.lower() if a in vowels]

    return new

print(remove_vowels(sentence))
print(remove_vowels_comp(sentence))

