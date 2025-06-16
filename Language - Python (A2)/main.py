from utils import load_file, save_file, find_athletes_by_name, delete_athlete_by_name, display_chart_level1, display_chart_leaf, display_salary_level1, display_salary_leaf, display_endorsements
from athlete import Athlete
from ball import BasketballPlayer, FootballPlayer
from hockey import HockeyPlayer
from swimmer import Swimmer


def print_stats(athletes):
    """
    Print summary statistics about the athletes.

    Displays:
    - Total number of athletes
    - Counts by sport (Hockey, Basketball, Football, Swimmers)
    - Endorsement counts for ball players
    - Goals scored by hockey players (if > 0)
    - Touchdowns by football players (if > 0)
    """

    print(f"\nStatistics:")
    print(f"{'-'*30}")
    print(f"{len(athletes)} athletes")

    hockey = [a for a in athletes if isinstance(a, HockeyPlayer)]
    basketball = [a for a in athletes if isinstance(a, BasketballPlayer)]
    football = [a for a in athletes if isinstance(a, FootballPlayer)]
    swimmer = [a for a in athletes if isinstance(a, Swimmer)]

    print(f"{len(hockey)} Hockey Players")
    print(f"{len(basketball) + len(football)} Ball Players ({len(basketball)} Basketball and {len(football)} Football)")
    print(f"{len(swimmer)} Swimmers")

    # Endorsement counts
    endorsements = {}
    for a in basketball + football:
        if a.endorsement:
            endorsements[a.endorsement] = endorsements.get(a.endorsement, 0) + 1
    print(f"\nEndorsements:")
    for k in sorted(endorsements):
        print(f"{k} ({endorsements[k]})")

    # Goals calculations
    print(f"\nGoals scored:")
    scored = sorted([a for a in hockey if a.goals_scored > 0],
                    key=lambda x: (-x.goals_scored, x.name))
    for a in scored:
        print(f"{a.goals_scored} {a.name}")

    # Touchdowns scored
    print(f"\nTouchdowns:")
    td = sorted([a for a in football if a.touchdowns > 0],
                key=lambda x: (-x.touchdowns, x.name))
    for a in td:
        print(f"{a.touchdowns} {a.name}")

    print("")


def athlete_info(athletes):

    """
    Prompt user for an athlete's name and display detailed information.

    - Searches for athletes by name (case-insensitive substring match)
    - Prints stats and endorsement information for each match
    """
     
    name = input("Enter athlete name: ")
    matches = find_athletes_by_name(athletes, name)
    if not matches:
        print("No such athlete.")
        return

    for a in matches:
        a.printStats()
        a.printEndorsement()
        print("")


def main():

    """
    Entry point of the application.

    Provides a command-line menu to:
    - Load athletes from a file
    - View statistics
    - Delete an athlete
    - Save changes
    - View individual athlete info
    - Display various charts
    - Exit the program (with unsaved change warning)
    """
    
    athletes = []
    filename = None
    unsaved_changes = False

    while True:
        print("\nMenu:")
        print("1. Load File")
        print("2. Print Stats")
        print("3. Delete Athlete")
        print("4. Save File")
        print("5. Athlete Info")
        print("6. Display Chart")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            filename = input("Filename to load: ")
            athletes = load_file(filename)
            unsaved_changes = False

        elif choice == "2":
            print_stats(athletes)

        elif choice == "3":
            name = input("Enter name to delete: ")
            athletes = delete_athlete_by_name(athletes, name)
            unsaved_changes = True

        elif choice == "4":
            if filename:
                save_file(filename, athletes)
                unsaved_changes = False
            else:
                print("No file loaded.")

        elif choice == "5":
            athlete_info(athletes)

        elif choice == "6":
            print("\nChart Menu:")
            print("1. Number of Athletes (level 1)")
            print("2. Number of Athletes (leaf level)")
            print("3. Athletes Salaries (level 1)")
            print("4. Athletes Salaries (leaf level)")
            print("5. Endorsements")
            sub_choice = input("Choose chart type: ")


            if sub_choice == "1":
                display_chart_level1(athletes)
            elif sub_choice == "2":
                display_chart_leaf(athletes)
            elif sub_choice == "3":
                display_salary_level1(athletes)
            elif sub_choice == "4":
                display_salary_leaf(athletes)
            elif sub_choice == "5":
                display_endorsements(athletes)
            else:
                print("Invalid chart option.")


        elif choice == "7":
            if unsaved_changes:
                confirm = input("Unsaved changes will be lost. Exit? (yes/no): ")
                if confirm != "yes":
                    continue
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
