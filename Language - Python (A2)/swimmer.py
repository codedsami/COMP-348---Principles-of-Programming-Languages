from athlete import Athlete
from helpers import safe_int, safe_float



class Swimmer(Athlete):
    """
    Represents a swimmer with specific attributes like stroke style and personal best time.

    Attributes:
        stroke_style (str): The swimmer's primary stroke style.
        personal_best_time (float or None): Swimmer's personal best time in seconds.

    Class Attributes:
        swimmer_count (int): Tracks the number of Swimmer instances created.
    """
    swimmer_count = 0

    def __init__(self, name, age, stroke_style, country=None, salary=None, personal_best_time=None):
        """
    Initialize a Swimmer instance.

    Args:
        name (str): Swimmer's name.
        age (int): Swimmer's age.
        stroke_style (str): Primary stroke style (e.g., freestyle, butterfly).
        country (str, optional): Country of origin.
        salary (float or str, optional): Swimmer's salary.
        personal_best_time (float or str, optional): Best swim time.
    """
        super().__init__(name, age, country, salary)
        self.stroke_style = stroke_style
        self.personal_best_time = safe_float(personal_best_time)

        Swimmer.swimmer_count += 1
        print(f"Swimmer '{self.name}', {self.age} created; total #of swimmers {Swimmer.swimmer_count}.")

    @staticmethod
    def parse(text):
        """
    Create a Swimmer instance from a formatted string.

    Expected format:
        "Swimmer:<name>,<age>,<stroke_style>,<country>,<salary>,<personal_best_time>"

    Args:
        text (str): Input string with swimmer details.

    Returns:
        Swimmer or None: Parsed Swimmer object or None if parsing fails.
    """
        try:
            data = text.split(":", 1)[1].split(",")

            while data and data[-1].strip() == "":
                data.pop()

            while len(data) < 6:
                data.append(None)
            data = data[:6]  

            data = [None if d is None or str(d).strip().lower() == "none" or d.strip() == "" else d.strip() for d in data]

            name, age, stroke, country, salary, best_time = data

            return Swimmer(name, age, stroke, country, salary, best_time)
        except Exception as e:
            print(f"Error parsing Swimmer: {e}")
            return None


    def printStats(self):
       """
    Print the swimmer’s stroke style and personal best time.
    Displays 'N/A' if a value is missing.
    """
       print(f"{self.name} — Stroke: {self.stroke_style if self.stroke_style is not None else 'N/A'}, "
          f"Best Time: {self.personal_best_time if self.personal_best_time is not None else 'N/A'}")

    def printEndorsement(self):
        """
    Placeholder for endorsement info.
    Inherits and calls the parent Athlete class’s endorsement method.
    """
        return super().printEndorsement()
