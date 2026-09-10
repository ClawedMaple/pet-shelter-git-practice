"""Run a short demonstration of the pet shelter classes."""

from pet import Pet
from shelter import Shelter


def main() -> None:
    shelter = Shelter("Desert Paws")

    shelter.add_pet(Pet("Milo", "cat", 4))
    shelter.add_pet(Pet("Luna", "dog", 9))
    shelter.add_pet(Pet("Kiwi", "bird", 2))

    print(f"Welcome to {shelter.name}!")
    for description in shelter.list_pets():
        print(f"- {description}")

    selected_pet = shelter.find_pet("Luna")
    if selected_pet is not None:
        print(selected_pet.celebrate_birthday())


if __name__ == "__main__":
    main()
