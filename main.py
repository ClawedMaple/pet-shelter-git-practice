"""Run a short demonstration of the pet shelter classes."""

from pet import Pet
from shelter import Shelter


def main() -> None:
    shelter = Shelter("Desert Paws")

    shelter.add_pet(Pet("Milo", "cat", 4))
    shelter.add_pet(Pet("Luna", "dog", 9))
    shelter.add_pet(Pet("Kiwi", "bird", 2))

    print(f"There are {shelter.pet_count()} pets in the shelter.")

    print(f"Welcome to {shelter.name}!")
    for description in shelter.list_pets():
        print(f"- {description}")

    selected_pet = shelter.find_pet("Luna")
    if selected_pet is not None:
        print(selected_pet.celebrate_birthday())
        print(F"Is Luna a senior pet? {'Yes' if selected_pet.is_senior() else 'No'}")

    adopted_pet = shelter.adopt_pet("Luna")
    if adopted_pet is not None:
        print(f"Congratulations! You have adopted {adopted_pet.name}!")
    
    print(f"There are {shelter.pet_count()} pets in the shelter.")

if __name__ == "__main__":
    main()

# Shhh! I'm hiding in this comment so that I can get staged!
