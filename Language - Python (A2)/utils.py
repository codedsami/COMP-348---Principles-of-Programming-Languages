import matplotlib.pyplot as plt
from hockey import HockeyPlayer
from swimmer import Swimmer
from ball import BasketballPlayer, FootballPlayer
from athlete import Athlete
from helpers import safe_int, safe_float



def load_file(filename):
    """
    Loads athlete data from a text file.

    Each line is expected to start with the class name (e.g., "Swimmer:", "HockeyPlayer:")
    followed by comma-separated values appropriate for the class.

    Args:
        filename (str): Path to the input file.

    Returns:
        list: A list of instantiated athlete objects.
    """
    athletes = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                if line.startswith("HockeyPlayer:"):
                    athlete = HockeyPlayer.parse(line)
                elif line.startswith("Swimmer:"):
                    athlete = Swimmer.parse(line)
                elif line.startswith("BasketballPlayer:"):
                    athlete = BasketballPlayer.parse(line)
                elif line.startswith("FootballPlayer:"):
                    athlete = FootballPlayer.parse(line)
                else:
                    athlete = None

                if athlete:
                    athletes.append(athlete)

        print(f"\nLoaded {len(athletes)} athletes from {filename}\n")
        return athletes
    except FileNotFoundError:
        print("File not found.")
        return []


def save_file(filename, athletes):
    """
    Saves athlete data to a file in the format expected by the loader.

    Prompts the user before overwriting.

    Args:
        filename (str): Path to the output file.
        athletes (list): List of athlete objects to save.
    """
    confirm = input(f"Are you sure you want to overwrite {filename}? (yes/no): ").strip().lower()
    if confirm != "yes":
        print("Save cancelled.")
        return

    try:
        with open(filename, 'w') as f:
            for a in athletes:
                line = stringify_athlete(a)
                if line:
                    f.write(line + "\n")
        print("File saved successfully.")
    except Exception as e:
        print(f"Error saving file: {e}")


def stringify_athlete(athlete):
    """
    Converts an athlete object into a single-line string representation.

    Args:
        athlete (Athlete): The athlete object.

    Returns:
        str: A formatted string representing the athlete, or empty string if unknown type.
    """
    # singleline text representation like the input file
    if isinstance(athlete, HockeyPlayer):
        return f"HockeyPlayer: {athlete.name},{athlete.age},{athlete.country},{athlete.salary}," \
               f"{athlete.position.name if athlete.position else ''},{athlete.goals_scored},{athlete.stick_brand},{athlete.skates_size}"
    elif isinstance(athlete, Swimmer):
        return f"Swimmer: {athlete.name},{athlete.age},{athlete.stroke_style},{athlete.country},{athlete.salary},{athlete.personal_best_time}"
    elif isinstance(athlete, BasketballPlayer):
        return f"BasketballPlayer: {athlete.name},{athlete.age},{athlete.team_name},{athlete.jersey_number}," \
               f"{athlete.country},{athlete.salary},{athlete.endorsement},{athlete.three_point_pct},{athlete.rebounds}"
    elif isinstance(athlete, FootballPlayer):
        return f"FootballPlayer: {athlete.name},{athlete.age},{athlete.team_name},{athlete.jersey_number}," \
               f"{athlete.country},{athlete.salary},{athlete.endorsement},{athlete.touchdowns},{athlete.passing_yards}"
    return ""


def find_athletes_by_name(athletes, name):
    """
    Finds all athletes with a given name.

    Args:
        athletes (list): List of athlete objects.
        name (str): The name to search for.

    Returns:
        list: Athletes with matching name.
    """
    return [a for a in athletes if a.name == name]


def delete_athlete_by_name(athletes, name):
    """
    Deletes all athletes with the specified name after user confirmation.

    Args:
        athletes (list): List of athlete objects.
        name (str): Name of the athlete(s) to delete.

    Returns:
        list: Updated list with specified athletes removed.
    """
    matches = find_athletes_by_name(athletes, name)
    if not matches:
        print("No athlete found with that name.")
        return athletes

    print(f"Found {len(matches)} athlete(s) with the name '{name}'.")
    confirm = input("Are you sure you want to delete all? (yes/no): ").strip().lower()
    if confirm != "yes":
        print("Deletion cancelled.")
        return athletes

    return [a for a in athletes if a.name != name]


def display_chart_level1(athletes):
    """
    Displays a pie chart showing the number of athletes for each leaf-level subclass:
    HockeyPlayer, BasketballPlayer, FootballPlayer, and Swimmer.
    """
    from ball import BallPlayer  #  importing here to avoid circular import
    labels = []
    sizes = []

    count = {
        "HockeyPlayer": sum(isinstance(a, HockeyPlayer) for a in athletes),
        "BallPlayer": sum(isinstance(a, BallPlayer) for a in athletes),
        "Swimmer": sum(isinstance(a, Swimmer) for a in athletes),
    }

    for label, size in count.items():
        if size > 0:
            labels.append(label)
            sizes.append(size)

    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title("Number of Athletes (Level 1)")
    plt.show()


def display_chart_leaf(athletes):
    """
    Displays a pie chart showing the number of athletes for each leaf-level subclass:
    HockeyPlayer, BasketballPlayer, FootballPlayer, and Swimmer.
    """
    from ball import BasketballPlayer, FootballPlayer
    from hockey import HockeyPlayer
    from swimmer import Swimmer

    count = {
        "HockeyPlayer": sum(isinstance(a, HockeyPlayer) for a in athletes),
        "BasketballPlayer": sum(isinstance(a, BasketballPlayer) for a in athletes),
        "FootballPlayer": sum(isinstance(a, FootballPlayer) for a in athletes),
        "Swimmer": sum(isinstance(a, Swimmer) for a in athletes),
    }

    labels = [k for k, v in count.items() if v > 0]
    sizes = [v for v in count.values() if v > 0]

    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title("Number of Athletes (Leaf Level)")
    plt.show()


def display_salary_level1(athletes):
    """
    Displays a pie chart of average salary per top-level class:
    HockeyPlayer, BallPlayer, and Swimmer.
    """
    from ball import BallPlayer
    from hockey import HockeyPlayer
    from swimmer import Swimmer

    groups = {
        "HockeyPlayer": [a.salary for a in athletes if isinstance(a, HockeyPlayer) and a.salary],
        "BallPlayer": [a.salary for a in athletes if isinstance(a, BallPlayer) and a.salary],
        "Swimmer": [a.salary for a in athletes if isinstance(a, Swimmer) and a.salary],
    }

    labels = []
    averages = []

    for k, salaries in groups.items():
        if salaries:
            avg = sum(salaries) / len(salaries)
            labels.append(k)
            averages.append(avg)

    plt.pie(averages, labels=labels, autopct='%1.1f%%')
    plt.title("Average Salary by Class (Level 1)")
    plt.show()


def display_salary_leaf(athletes):
    """
    Displays a pie chart of average salary for each leaf-level subclass:
    HockeyPlayer, BasketballPlayer, FootballPlayer, and Swimmer.
    """
    from ball import BasketballPlayer, FootballPlayer
    from hockey import HockeyPlayer
    from swimmer import Swimmer

    groups = {
        "HockeyPlayer": [a.salary for a in athletes if isinstance(a, HockeyPlayer) and a.salary],
        "BasketballPlayer": [a.salary for a in athletes if isinstance(a, BasketballPlayer) and a.salary],
        "FootballPlayer": [a.salary for a in athletes if isinstance(a, FootballPlayer) and a.salary],
        "Swimmer": [a.salary for a in athletes if isinstance(a, Swimmer) and a.salary],
    }

    labels = []
    averages = []

    for k, salaries in groups.items():
        if salaries:
            avg = sum(salaries) / len(salaries)
            labels.append(k)
            averages.append(avg)

    plt.pie(averages, labels=labels, autopct='%1.1f%%')
    plt.title("Average Salary by Class (Leaf Level)")
    plt.show()


def display_endorsements(athletes):
    """
    Displays a pie chart showing the count of ballplayers grouped by endorsement brand.

    Only applies to BasketballPlayer and FootballPlayer instances with endorsement deals.
    """
    from ball import BasketballPlayer, FootballPlayer

    endorsements = {}

    for a in athletes:
        if isinstance(a, (BasketballPlayer, FootballPlayer)) and a.endorsement:
            key = a.endorsement
            endorsements[key] = endorsements.get(key, 0) + 1

    if not endorsements:
        print("No endorsements found.")
        return

    labels = list(endorsements.keys())
    sizes = list(endorsements.values())

    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title("Number of Ballplayers per Endorsement")
    plt.show()



