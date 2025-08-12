#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    approved_breeds = [
        "Mastiff", "Chihuahua", "Corgi", "Shar Pei",
        "Beagle", "French Bulldog", "Pug", "Pointer"
    ]

    def __init__(self, name="Fido", breed="Mutt"):
        # First set name
        self.name = name
        # Only attempt breed if _name exists (valid name was set)
        if hasattr(self, "_name"):
            self.breed = breed

    # name property
    def get_name(self):
        return self._name

    def set_name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
        else:
            print("Name must be string between 1 and 25 characters.")

    name = property(get_name, set_name)

    # breed property
    def get_breed(self):
        return self._breed

    def set_breed(self, value):
        if value in Dog.approved_breeds:
            self._breed = value
        else:
            print("Breed must be in list of approved breeds.")

    breed = property(get_breed, set_breed)


    pass
