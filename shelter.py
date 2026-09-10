"""Shelter collection for the Git foundations practice project."""

from pet import Pet


class Shelter:
    """Manage the pets currently living at one shelter."""

    def __init__(self, name: str) -> None:
        self.name = name
        self.pets: list[Pet] = []

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to the shelter."""
        self.pets.append(pet)

    def list_pets(self) -> list[str]:
        """Return descriptions for every pet in the shelter."""
        return [pet.describe() for pet in self.pets]

    def find_pet(self, name: str) -> Pet | None:
        """Find a pet by name, ignoring capitalization."""
        for pet in self.pets:
            if pet.name.lower() == name.lower():
                return pet
        return None
