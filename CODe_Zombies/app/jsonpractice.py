print("Hello World!")


import json

characters = {
    "dempsey": {
        "name": "Dempsey",
        "hp": 150,
        "favored_weapon": "ar",
        "has_juggernog": False,
        "has_double_tap": False,
        "has_deadshot_daiquiri": False
    },
    "nikolai": {
        "name": "Nikolai",
        "hp": 150,
        "favored_weapon": "shotgun",
        "has_juggernog": False,
        "has_double_tap": False,
        "has_deadshot_daiquiri": False
    },
    "richtofen": {
        "name": "Dr. Richtofen",
        "hp": 150,      
        "favored_weapon": "smg",
        "has_juggernog": False,
        "has_double_tap": False,
        "has_deadshot_daiquiri": False
    }
}

with open("data/test.json", "w") as f:
    json.dump(characters, f, indent=4)


# Close the file when done
f.close()

with open("data/test.json", "r") as f:
    data = json.load(f)
    print(data)

print("Printing Dempsey's name:-------------")
print(data["dempsey"]["name"])