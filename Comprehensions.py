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


def water_temp_list(organized_data):
    water_temp = [(i[4]) for i in organized_data]
    water_temp_list = (water_temp[1:])
    return water_temp_list


def float_water_temp_list(water_temp_list):
    float_water_temp = [float(i) for i in water_temp_list]
    return float_water_temp


def fahrenheit_temp_list(float_water_temp):
    fahrenheit_temp = [int((i * 9/5 + 32)) for i in float_water_temp]
    return (fahrenheit_temp)


# keys = []

# first_line = [row.split(",") for row in first_line]

# for i in first_line:
    # for index, header in enumerate(i):
        # keys.append(header)

date = []
wave_height = []

for i in organized_data:
    date.append(i[5])
    wave_height.append(i[1])

date_wave_height = {date: float(wave_height[index]) for index, date in enumerate(date)}

#for keys, values in date_wave_height.items():
    #print(sum(values))

grades = {'Gale': {'Homework 1': 88, 'Homework 2': 76},
          'Jordan': {'Homework 1': 92, 'Homework 2': 87},
          'Peyton': {'Homework 1': 84, 'Homework 2': 77},
          'River': {'Homework 1': 85, 'Homework 2': 91}}

Gale = (grades.get('Gale', {}).get('Homework 1'))
Jordan = (grades.get('Jordan', {}).get('Homework 1'))
Peyton = (grades.get('Peyton', {}).get('Homework 1'))
River = (grades.get('River', {}).get('Homework 1'))

total = (Gale + Jordan + Peyton + River) / 4

print(total)
print(date_wave_height)
print(water_temp_list(organized_data))
print(float_water_temp_list(water_temp_list(organized_data)))
print(fahrenheit_temp_list(float_water_temp_list(water_temp_list(organized_data))))
