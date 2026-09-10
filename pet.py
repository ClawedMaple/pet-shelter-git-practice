"""Pet model for the Git foundations practice project."""


class Pet:
    """Represent one pet living at the shelter."""

    def __init__(self, name: str, species: str, age: int) -> None:
        self.name = name
        self.species = species
        self.age = age

    def is_senior(self) -> bool:
        """Return True if the pet is considered a senior (age 8 or older)."""
        return self.age >= 8

    def describe(self) -> str:
        """Return a readable description of the pet."""
        if self.is_senior():
            return f"{self.name} is a senior, {self.age}-year-old {self.species}."
        return f"{self.name} is a {self.age}-year-old {self.species}."

    def celebrate_birthday(self) -> str:
        """Increase the pet's age and return a birthday message."""
        self.age += 1
        return f"Happy birthday, {self.name}! {self.name} is now {self.age}."

    def __str__(self) -> str:
        return self.describe()
