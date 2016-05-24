import datetime
from itertools import zip_longest

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


def fahrenheit_temp_list(water_temp_list):
    fahrenheit_temp = [int((i * 9/5 + 32)) for i in water_temp_list]
    return (fahrenheit_temp)


date = []
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
wave_height = []
days_of_week = []

for i in organized_data:
    date.append(i[5])
    wave_height.append(i[1])


for d in date:
    date_list = [int(day) for day in (d.split("-"))]
    date_obj = datetime.date(*date_list)
    day_of_week = date_obj.weekday()
    dow_list = (days[day_of_week])
    days_of_week.append(dow_list)


wave_average = {float(wh): [dow] for wh, dow in zip_longest(wave_height, days_of_week)}

Sunday = []
Monday = []
Tuesday = []
Wednesday = []
Thursday = []
Friday = []
Saturday = []

for key, value in wave_average.items():
    for i in value:
        if i == "Sunday":
            Sunday.append(key)
        if i == "Monday":
            Monday.append(key)
        if i == "Tuesday":
            Tuesday.append(key)
        if i == "Wednesday":
            Wednesday.append(key)
        if i == "Thursday":
            Thursday.append(key)
        if i == "Friday":
            Friday.append(key)
        if i == "Saturday":
            Saturday.append(key)

day_wave_avg = (sum(Monday) / len(Monday), sum(Tuesday) / len(Tuesday), sum(Wednesday) / len(Wednesday),\
      sum(Thursday) / len(Thursday), sum(Friday) / len(Friday),
      sum(Saturday) / len(Saturday), sum(Sunday) / len(Sunday))

day_wave_avg_dict = {day: float(day_wave_avg[index]) for index, day in enumerate(days)}


def get_wave_heights():
    date_wave_height = {date: float(wave_height[index]) for index, date in enumerate(date)}

    return date_wave_height


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

homework1_average = (Gale + Jordan + Peyton + River) / 4

grades = [v["Homework 1"] for k, v in grades.items()]

print(remove_vowels_comp(sentence))
print(day_wave_avg_dict)
print(homework1_average)
print(water_temp_list(organized_data))
print(float_water_temp_list(water_temp_list(organized_data)))
print(fahrenheit_temp_list(float_water_temp_list(water_temp_list(organized_data))))
print(get_wave_heights())


