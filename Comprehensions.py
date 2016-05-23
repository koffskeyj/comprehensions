import string

sentence = "List comprehensions are the greatest!"
opened_file = open("water_temp")
data = opened_file.read().lower()


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

data_set = data.replace(" ", "").split()
organized_data = [row.split(",") for row in data_set]


water_temp = [(i[4]) for i in organized_data]
water_temp_list = (water_temp[1:])


float_water_temp_list = [float(i) for i in water_temp_list]


#print(accurate_water_temp)



