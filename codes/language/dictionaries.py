""" Learning Python dictionary
"""

from pprint import pprint

# elements are in key-value pair
user_dictionary = {
    "username": "brian",
    "name": "Thandokuhle Brian Msane",
    "age": 77,
    "fav_number": 7,
    "sports": "soccer",
    "team": "Manchester United",
}

school = {
    "student_id": 777,
    "level": 4,
    "major": ["information technology", "computer science", "data science"],
}

# reference a specific key
user_dictionary.get("username")

# updating a dictionary (adding key-value pairs)
# the attributes of a dictionary can be any format
user_dictionary["college"] = "UNESWA"
user_dictionary.update({"gender": "M"})
user_dictionary.update({"school": school})

# remove key-value pair from the dictionary
user_dictionary.pop("age")
user_dictionary.keys()

# use pprint to print a nicer and readable format of the dict
pprint(user_dictionary)

# delete the dictionary
del school  # or school.clear()


# looping through the dictionary

my_dict: dict = user_dictionary.copy()  # avoid messing with the original dict
for key, value in my_dict.items():
    print(str(key) + "\t" + str(value))
