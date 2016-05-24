import string

sentence = "List comprehensions are the greatest!"
with open("water_temp") as f:
    first_line = [f.readline().replace("\n", "")]
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


data_set = data.replace(" ", "").split()

organized_data = [row.split(",") for row in data_set]
print(organized_data)


def water_temp_list(organized_data):
    water_temp = [(i[4]) for i in organized_data]
    water_temp_list = (water_temp[1:])
    return water_temp_list


def float_water_temp_list(water_temp_list):
    float_water_temp = [float(i) for i in water_temp_list]
    return float_water_temp


def fahrenheit_temp_list(float_water_temp):
    fahrenheit_temp = [int((i * 9/5 + 32)) for i in float_water_temp]
    print(fahrenheit_temp)


keys = []

first_line = [row.split(",") for row in first_line]

for i in first_line:
    for index, header in enumerate(i):
        keys.append(header)

print(keys)

