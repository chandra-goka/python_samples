
persons = {
    'user_name':'chandra',
    'first_name':'chandra shekhar',
    'last_name':'goka'
}

#Looping key,values
for key,value in persons.items():
    print(f"Key: {key} - Value: {value}")

favorite_subjects={
    'chandra':'Computers',
    'panvith':'Physics',
    'jon':'Mathematics',
    'robert':'Computers'
}

for name,fav_subject in favorite_subjects.items():
    print(f"{name} likes {fav_subject}")

#Order
for name,fav_subject in sorted(favorite_subjects.items()):
    print(f"{name} likes {fav_subject}")

#Keys in Order

for name in sorted(favorite_subjects.keys()):
    print(name)

#Values in Order

for fav_subject in sorted(favorite_subjects.values()):
    print(fav_subject)

#Remove duplicates in values

for fav_subject in sorted(set(favorite_subjects.values())):
    print(fav_subject)