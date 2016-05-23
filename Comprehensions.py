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
    new = "".join([a for a in b.lower() if a not in vowels])

    return new

print(remove_vowels(sentence))
print(remove_vowels_comp(sentence))

def water_temp_list():
    headers = ["ID", "Wave Height", "Wave Period", "Avg Waves Per Second",
               "Water Temp", "Date"]
    info = 