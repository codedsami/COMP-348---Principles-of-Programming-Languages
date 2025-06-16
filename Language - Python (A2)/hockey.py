from athlete import Athlete
from enum import Enum
from helpers import safe_int, safe_float



class HockeyPosition(Enum):
   
    Forward = "Forward"
    Defenseman = "Defenseman"
    Goalie = "Goalie"


class HockeyPlayer(Athlete):
    """
    Represents a hockey player, subclass of Athlete.

    Attributes:
        position (HockeyPosition or None): Player's position on the team.
        goals_scored (int or None): Number of goals scored by the player.
        stick_brand (str): Brand of the hockey stick.
        skates_size (int or None): Size of the player's skates.

    Class Attributes:
        hockey_count (int): Class-level count of HockeyPlayer instances.
    """

    hockey_count = 0

    def __init__(self, name, age, country=None, salary=None, position=None,
                 goals_scored=None, stick_brand=None, skates_size=None):
        super().__init__(name, age, country, salary)
        """
        Initialize a HockeyPlayer instance.

        Args:
            name (str): Name of the athlete.
            age (int): Age of the athlete.
            country (str, optional): Country of the athlete.
            salary (float, optional): Salary of the athlete.
            position (str, optional): Position name (e.g., "Forward").
            goals_scored (int or str, optional): Number of goals scored.
            stick_brand (str, optional): Brand of the stick.
            skates_size (int or str, optional): Skate size.
        """
        self.position = HockeyPosition[position] if position else None
        self.goals_scored = safe_int(goals_scored)
        self.stick_brand = stick_brand if stick_brand else "Unknown"
        self.skates_size = safe_int(skates_size)

        HockeyPlayer.hockey_count += 1
        print(f"Hockey Player '{self.name}', {self.age} created; total #of hockey players {HockeyPlayer.hockey_count}.")

    @staticmethod
    def parse(text):
        """
        Parse a text line to create a HockeyPlayer object.

        Expected format:
            "Hockey:<name>,<age>,<country>,<salary>,<position>,<goals>,<stick_brand>,<skates_size>"

        Args:
            text (str): Input string containing athlete information.

        Returns:
            HockeyPlayer or None: A new HockeyPlayer instance, or None on failure.
        """
        try:
            data = text.split(":", 1)[1].split(",")

            while data and data[-1].strip() == "":
                data.pop()

            while len(data) < 8:
                data.append(None)

            data = data[:8]
            data = [None if d is None or str(d).strip().lower() == "none" or d.strip() == "" else d.strip() for d in data]


            return HockeyPlayer(*data)
        except Exception as e:
            print(f"Error parsing BasketballPlayer: {e}")
            return None
        
    
    def printStats(self):
      """
      Print hockey-specific statistics, including goals, stick brand, and skate size.
      """
      print(f"{self.name} — Goals scored: {self.goals_scored if self.goals_scored is not None else 'N/A'}, "
          f"Stick Brand: {self.stick_brand if self.stick_brand is not None else 'N/A'}, "
          f"Skate size: {self.skates_size if self.skates_size is not None else 'N/A'}")

    def printEndorsement(self):
        """
        Display endorsement information. Inherits behavior from Athlete.
        """
        super().printEndorsement()

