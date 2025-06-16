class Athlete:
    """
    Base class representing a generic athlete.

    Attributes:
        name (str): Name of the athlete.
        age (int): Age of the athlete.
        country (str): Country of the athlete. Defaults to 'Unknown' if not provided.
        salary (float or None): Salary of the athlete. None if not provided.

    Class Attributes:
        athlete_count (int): Tracks the total number of Athlete instances created.
    """

    athlete_count = 0

    def __init__(self, name, age, country=None, salary=None):
        """
        Initialize a new Athlete instance.

        Args:
            name (str): Athlete's name.
            age (int): Athlete's age.
            country (str, optional): Country of origin. Defaults to 'Unknown' if not provided.
            salary (float, optional): Salary. Set to None if not provided.
        """
        self.name = name
        self.age = int(age)
        self.country = country if country else "Unknown"
        self.salary = float(salary) if salary else None

        Athlete.athlete_count += 1
        print(f"Athlete '{self.name}', {self.age} created; total #of athletes {Athlete.athlete_count}.")

    def printStats(self):
        """
        Placeholder method to print athlete statistics.
        Intended to be overridden by subclasses.
        """
        pass

    def printEndorsement(self):
        """
        Placeholder method to print athlete endorsement details.
        Intended to be overridden by subclasses.
        """
        pass
