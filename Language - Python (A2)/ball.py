from athlete import Athlete
from helpers import safe_int, safe_float



class BallPlayer(Athlete):
    """
    Base class for ball-based athletes such as basketball and football players.

    Attributes:
        team_name (str): Name of the team the player belongs to.
        jersey_number (int or None): Jersey number of the player.
        endorsement (str or None): Endorsement deal name.

    Class Attributes:
        ballplayer_count (int): Tracks the number of BallPlayer instances created.
    """
    ballplayer_count = 0

    def __init__(self, name, age, country=None, salary=None, team_name=None, jersey_number=None, endorsement=None):
        super().__init__(name, age, country, salary)
        """
        Initialize a BallPlayer instance.

        Args:
            name (str): Player's name.
            age (int): Player's age.
            country (str, optional): Country of origin.
            salary (float, optional): Salary of the player.
            team_name (str, optional): Name of the team.
            jersey_number (int or str, optional): Jersey number.
            endorsement (str, optional): Endorsement deal.
        """
        self.team_name = team_name
        self.jersey_number = int(jersey_number) if jersey_number else None
        self.endorsement = endorsement

        BallPlayer.ballplayer_count += 1
        print(f"Ball Player '{self.name}', {self.age} created; total #of ball players {BallPlayer.ballplayer_count}.")

    def printEndorsement(self):
        """
        Print the athlete’s endorsement deal or 'None' if not available.
        """
        print(f"Endorsement deal: {self.endorsement if self.endorsement else 'None'}")


class BasketballPlayer(BallPlayer):
    """
        Represents a basketball player with specific statistics.

        Attributes:
            three_point_pct (float or None): 3-point shooting percentage.
            rebounds (int or None): Number of rebounds.

        Class Attributes:
            basketball_count (int): Tracks number of BasketballPlayer instances created.
        """
    basketball_count = 0

    def __init__(self, name, age, team_name=None, jersey_number=None, country=None, salary=None,
                 endorsement=None, three_point_pct=None, rebounds=None):
        
        
        super().__init__(name, age, country, salary, team_name, jersey_number, endorsement)
        """
        Initialize a BasketballPlayer instance.

        Args:
            name (str): Player's name.
            age (int): Player's age.
            team_name (str, optional): Team name.
            jersey_number (int or str, optional): Jersey number.
            country (str, optional): Country of origin.
            salary (float, optional): Player's salary.
            endorsement (str, optional): Endorsement deal.
            three_point_pct (float or str, optional): 3PT percentage.
            rebounds (int or str, optional): Rebound count.
        """

        self.three_point_pct = safe_float(three_point_pct)
        self.rebounds = safe_int(rebounds)

        BasketballPlayer.basketball_count += 1
        print(f"Basketball Player '{self.name}', {self.age} created; total #of basketball players {BasketballPlayer.basketball_count}.")

    @staticmethod

    def parse(text):
        """
    Create a BasketballPlayer instance from a formatted string.

    Expected format:
        "Basketball:<name>,<age>,<team>,<jersey>,<country>,<salary>,<endorsement>,<3pt_pct>,<rebounds>"

    Args:
        text (str): Input string with player details.

    Returns:
        BasketballPlayer or None: Parsed instance or None if parsing fails.
    """
        try:
            data = text.split(":", 1)[1].split(",")

            while data and data[-1].strip() == "":
                data.pop()

            while len(data) < 9:
                data.append(None)

            data = data[:9]
            data = [None if d is None or str(d).strip().lower() == "none" or d.strip() == "" else d.strip() for d in data]


            return BasketballPlayer(*data)
        except Exception as e:
            print(f"Error parsing BasketballPlayer: {e}")
            return None


    def printStats(self):
      """
    Print the player's 3PT percentage and rebounds. Displays 'N/A' for missing values.
    """
      print(f"{self.name} — 3PT%: {self.three_point_pct if self.three_point_pct is not None else 'N/A'}, "
          f"Rebounds: {self.rebounds if self.rebounds is not None else 'N/A'}")

    def printEndorsement(self):
        """
    Print the player's endorsement deal.
    """
        super().printEndorsement()


class FootballPlayer(BallPlayer):
    """
    Represents a football player with specific statistics.

    Attributes:
        touchdowns (int or None): Number of touchdowns scored.
        passing_yards (int or None): Number of passing yards.

    Class Attributes:
        football_count (int): Tracks number of FootballPlayer instances created.
    """
    football_count = 0

    def __init__(self, name, age, team_name=None, jersey_number=None, country=None, salary=None,
                 endorsement=None, touchdowns=None, passing_yards=None):
        """
    Initialize a FootballPlayer instance.

    Args:
        name (str): Player's name.
        age (int): Player's age.
        team_name (str, optional): Team name.
        jersey_number (int or str, optional): Jersey number.
        country (str, optional): Country of origin.
        salary (float, optional): Player's salary.
        endorsement (str, optional): Endorsement deal.
        touchdowns (int or str, optional): Number of touchdowns.
        passing_yards (int or str, optional): Number of passing yards.
    """
        super().__init__(name, age, country, salary, team_name, jersey_number, endorsement)
        self.touchdowns = safe_int(touchdowns)
        self.passing_yards = safe_int(passing_yards)

        FootballPlayer.football_count += 1
        print(f"Football Player '{self.name}', {self.age} created; total #of football players {FootballPlayer.football_count}.")

    @staticmethod
    def parse(text):
        """
    Create a FootballPlayer instance from a formatted string.

    Expected format:
        "Football:<name>,<age>,<team>,<jersey>,<country>,<salary>,<endorsement>,<touchdowns>,<passing_yards>"

    Args:
        text (str): Input string with player details.

    Returns:
        FootballPlayer or None: Parsed instance or None if parsing fails.
    """
        try:
            data = text.split(":", 1)[1].split(",")

            while data and data[-1].strip() == "":
                data.pop()

            while len(data) < 9:
                data.append(None)

            data = data[:9]
            data = [None if d is None or str(d).strip().lower() == "none" or d.strip() == "" else d.strip() for d in data]


            return FootballPlayer(*data)
        except Exception as e:
            print(f"Error parsing BasketballPlayer: {e}")
            return None


    def printStats(self):
      """
    Print the player's touchdowns and passing yards. Displays 'N/A' for missing values.
    """
      print(f"{self.name} — Touchdowns: {self.touchdowns if self.touchdowns is not None else 'N/A'}, "
          f"Passing Yards: {self.passing_yards if self.passing_yards is not None else 'N/A'}")

    def printEndorsement(self):
        """
    Print the player's endorsement deal.
    """
        super().printEndorsement()
