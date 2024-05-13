class Cat:
    count_animals: int = 0

    def __init__(self, age: int, name: str = "Octavio") -> None:
        """Initialize a Cat instance."""
        self._name = name
        self._age = age
        Cat.count_animals += 1

    def birthday(self) -> None:
        """Update the cat's age by one."""
        self._age += 1

    @property
    def age(self) -> int:
        """Return the cat's age."""
        return self._age

    @age.setter
    def age(self, new_age: int) -> None:
        """Set the cat's age."""
        self._age = new_age
        
    @property
    def name(self) -> str:
        """Return the cat's name."""
        return self._name
    
    @name.setter
    def name(self, new_name: str) -> None:
        """Set the cat's name."""
        self._name = new_name


def main():
    garfield = Cat(8, "Garfield")
    gato = Cat(5)

    gato.birthday()
    print(garfield.name)
    print(gato.name)
    gato.name = "Gato"
    print(gato.name)
    print(Cat.count_animals)


if __name__ == '__main__':
    main()