# Mod 7 Project, CDC Program: Shelter Pet Inventory

class Pet:
    """This program is designed to build and append an inventory of pets in a shelter using private strings.
    It applies a user input menu to interact with the program and saves the inventory to a text file."""
    def __init__(self, name, breed, color, age, species):
        self.name = name
        self.breed = breed
        self.color = color
        self.age = age
        self.species = species

    def set_name(self, name):
        self.name = name

    def set_breed(self, breed):
        self.breed = breed

    def set_color(self, color):
        self.color = color

    def set_age(self, age):
        self.age = age

    def set_species(self, species):
        self.species = species

    def get_name(self):
        return self.name

    def get_breed(self):
        return self.breed

    def get_color(self):
        return self.color

    def get_age(self):
        return self.age

    def get_species(self):
        return self.species

    def add_pet(pet_list):
        name = input("Enter pet's name: ")
        breed = input('Enter breed: ')
        color = input('Enter color: ')
        try:
            age = int(input('Enter age: '))
        except ValueError:
            print('Error. Please use numbers only.')
        species = input('Enter Cat or Dog: ')
        pet_record = Pet(name, breed, color, age, species)
        pet_list.append(pet_record)
        print('New pet has been successfully added.')

    def remove_pet(pet_list):
        index = int(input('Enter the index number of pet to be removed: '))
        if index >= 0 and index < len(pet_list):
            name = pet_list[index].get_name()
            species = pet_list[index].get_species()
            pet_list.pop(index)
            print(name, species, 'has been removed from inventory.')
        else:
            print('Invalid index entry.')

    def update_pet(pet_list):
        index = int(input('Enter the index number of pet to be updated: '))
        if index >= 0 and index < len(pet_list):
            name = input('Enter updated name: ')
            breed = input('Enter updated breed: ')
            color = input('Enter updated color: ')
            try:
                age = int(input('Enter updated age: '))
            except ValueError:
                print('Error. Please use numbers only.')
            species = input('Enter updated species, Cat or Dog: ')
            pet_list[index].set_name(name)
            pet_list[index].set_breed(breed)
            pet_list[index].set_color(color)
            pet_list[index].set_age(age)
            pet_list[index].set_species(species)
            print(name, 'has been successfully updated')
        else:
            print('Invalid index entry.')

    def display_pets(pet_list):
        print('{:10} {:10} {:10} {:10} {:10} {:10}'.format('index#', 'NAME', 'BREED', 'COLOR', 'AGE', 'SPECIES'))
        for i in range(len(pet_list)):
            pet_record = pet_list[i]
            print('{:10} {:10} {:10} {:10} {:10} {:10}'.format(str(i), pet_record.get_name(), pet_record.get_breed(),
                pet_record.get_color(), str(pet_record.get_age()), str(pet_record.get_species())))


pet_list = []

while True:
    print('1. Add a pet')
    print('2. Remove a pet')
    print('3. Update a pet')
    print('4. Display all pets')
    print('5. Quit')
    menu = int(input(' Enter option 1-5: '))
    if menu == 1:
        Pet.add_pet(pet_list)
    elif menu == 2:
        Pet.remove_pet(pet_list)
    elif menu == 3:
        Pet.update_pet(pet_list)
    elif menu == 4:
        Pet.display_pets(pet_list)
    elif menu == 5:
        break
    else:
        print('Invalid option.')


file = open('pet_inventory.rtf', 'a')
for p in pet_list:
    file.write(str(p) + "\n")
file.close()
