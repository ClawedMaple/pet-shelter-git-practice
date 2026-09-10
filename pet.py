"""Pet model for the Git foundations practice project."""


class Pet:
    """Represent one pet living at the shelter."""

    def __init__(self, name: str, species: str, age: int) -> None:
        self.name = name
        self.species = species
        self.age = age

    def describe(self) -> str:
        """Return a readable description of the pet."""
        return f"{self.name} is a {self.age}-year-old {self.species}."

    def celebrate_birthday(self) -> str:
        """Increase the pet's age and return a birthday message."""
        self.age += 1
        return f"Happy birthday, {self.name}! {self.name} is now {self.age}."

    def __str__(self) -> str:
        return self.describe()
