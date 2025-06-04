#include <stdio.h>
#include <stdlib.h>
#include "data.h"
#include "budget.h"

#include <stdlib.h>

void clearScreen() {
#ifdef _WIN32
    system("cls");
#else
    system("clear");
#endif
}


int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <input_file>\n", argv[0]);
        return 1;
    }
    char *inputFileName = argv[1];
    Entry *entries = NULL;
    int entryCount = 0;

    if (!loadEntries(inputFileName, &entries, &entryCount)) {
        fprintf(stderr, "Failed to load entries.\n");
        return 1;
    }

    printf("Loaded %d entries from file.\n", entryCount);



    int choice;
    char input[100];
    do {

        clearScreen();

        printf("\nBudget Tracking System\n");
        printf("=====================\n");
        printf("1. Display all entries\n");
        printf("2. Expense Distribution\n");
        printf("3. Sort Entries\n");
        printf("4. Add Income/Expense Entry\n");
        printf("5. Modify Entry\n");
        printf("6. Filter by Month\n");
        printf("7. Exit\n");
        printf("8. Show Income Bar Chart (Extra Credit)\n");
        printf("Choice: ");
        fgets(input, sizeof(input), stdin);

        if (sscanf(input, "%d", &choice) != 1) {
            printf("Invalid input. Please enter a number between 1 and 7.\n");
            choice = 0; // invalid choice
            continue;
        }

        switch (choice) {
            case 1:
                displayAllEntries(entries, entryCount);
                break;
            case 2:
                showExpenseDistribution(entries, entryCount);
                break;
            case 3:
                sortEntries(entries, entryCount);
                break;
            case 4:
                addEntry(&entries, &entryCount);
                break;
            case 5:
                modifyEntry(entries, entryCount);
                break;
            case 6:
                filterByMonth(entries, entryCount);
                break;
            case 7:
                printf("Goodbye and thanks for using our budget tracker app!!!\n");
                break;
            case 8:
                showIncomeBarChart(entries, entryCount);
                break;

            default:
                printf("Invalid choice. Please try again.\n");
        }

        if (choice != 7) {
            printf("\nPress Enter to continue...");
            fgets(input, sizeof(input), stdin);  // waits for Enter
        }


    } while (choice != 7);

    //memory cleanup
    free(entries);

    return 0;
}
