#include <stdio.h>
#include "data.h"
#include <stdlib.h>
#include "ordering.h"
#include <string.h>
#include <time.h>





//option 1
void displayAllEntries(Entry *entries, int count) {
    printf("\nFinances Summary\n");
    printf("=================\n\n");
    printf("%-6s %-12s %-10s %-12s %-20s %-10s\n",
           "ID", "Date", "Type", "Category", "Description", "Amount");
    printf("--------------------------------------------------------------------------------------\n");

    for (int i = 0; i < count; i++) {
        printf("%-6d %-12s %-10s %-12s %-20s $%-.2f\n",
               entries[i].id,
               entries[i].date,
               entries[i].type,
               entries[i].category,
               entries[i].description,
               entries[i].amount);
    }
}


//option 2
void showExpenseDistribution(Entry *entries, int count) {
    float totalIncome = 0, totalExpenses = 0;
    float needs = 0, wants = 0;

    for (int i = 0; i < count; i++) {
        if (strcmp(entries[i].type, "income") == 0) {
            totalIncome += entries[i].amount;
        } else if (strcmp(entries[i].type, "expense") == 0) {
            totalExpenses += entries[i].amount;

            if (strcmp(entries[i].category, "Needs") == 0) {
                needs += entries[i].amount;
            } else if (strcmp(entries[i].category, "Wants") == 0) {
                wants += entries[i].amount;
            }
        }
    }

    float needsPercentExp = totalExpenses > 0 ? (needs / totalExpenses) * 100 : 0;
    float wantsPercentExp = totalExpenses > 0 ? (wants / totalExpenses) * 100 : 0;

    float needsPercentInc = totalIncome > 0 ? (needs / totalIncome) * 100 : 0;
    float wantsPercentInc = totalIncome > 0 ? (wants / totalIncome) * 100 : 0;

    float netBalance = totalIncome - totalExpenses;

    printf("\n===== Expense Distribution Report =====\n");
    printf("Total income: $%.2f\n", totalIncome);
    printf("Total Expense: $%.2f\n", totalExpenses);
    printf("Needs: $%.2f (%.2f%% of expenses, %.2f%% of income)\n", needs, needsPercentExp, needsPercentInc);
    printf("Wants: $%.2f (%.2f%% of expenses, %.2f%% of income)\n", wants, wantsPercentExp, wantsPercentInc);
    printf("Net Balance: $%.2f\n", netBalance);
    printf("======================================\n");
}


//option 3
void sortEntries(Entry *entries, int count) {
    int choice;
    printf("\nSort Menu\n");
    printf("1. Sort by id\n");
    printf("2. Sort by Date\n");
    printf("3. Sort by Amount\n");
    printf("4. Sort by Description\n");
    printf("Choice: ");
    scanf("%d", &choice);
    getchar(); // clear newline

    switch (choice) {
        case 1:
            qsort(entries, count, sizeof(Entry), compareByID);
            printf("sorted by ID.\n");
            break;
        case 2:
            qsort(entries, count, sizeof(Entry), compareByDate);
            printf("sorted by Date.\n");
            break;
        case 3:
            qsort(entries, count, sizeof(Entry), compareByAmount);
            printf("sorted by Amount.\n");
            break;
        case 4:
            qsort(entries, count, sizeof(Entry), compareByDescription);
            printf("sorted by Description.\n");
            break;
        default:
            printf("Invalid choice.\n");
            return;
    }

    displayAllEntries(entries, count);
}

#include <string.h>
#include <time.h>

//option 4
void addEntry(Entry **entries, int *count) {
    Entry newEntry;
    char input[100];
    char choice;

    // Generate ID
    int maxId = 0;
    for (int i = 0; i < *count; i++) {
        if ((*entries)[i].id > maxId) {
            maxId = (*entries)[i].id;
        }
    }
    newEntry.id = maxId + 1;

    // Ask for date
    printf("Use today's date? (y/n): ");
    fgets(input, sizeof(input), stdin);
    sscanf(input, " %c", &choice);

    if (choice == 'y' || choice == 'Y') {
        time_t t = time(NULL);
        struct tm *tm_info = localtime(&t);
        strftime(newEntry.date, sizeof(newEntry.date), "%Y-%m-%d", tm_info);
    } else {
        printf("Enter date (YYYY-MM-DD): ");
        fgets(newEntry.date, sizeof(newEntry.date), stdin);
        newEntry.date[strcspn(newEntry.date, "\n")] = 0; // Remove newline
    }

    // Type
    printf("Type (income/expense): ");
    fgets(newEntry.type, sizeof(newEntry.type), stdin);
    newEntry.type[strcspn(newEntry.type, "\n")] = 0;

    // Category
    printf("Category: ");
    fgets(newEntry.category, sizeof(newEntry.category), stdin);
    newEntry.category[strcspn(newEntry.category, "\n")] = 0;

    // Description
    printf("Description: ");
    fgets(newEntry.description, sizeof(newEntry.description), stdin);
    newEntry.description[strcspn(newEntry.description, "\n")] = 0;

    // Amount
    float amount;
    printf("Amount: $");
    fgets(input, sizeof(input), stdin);
    sscanf(input, "%f", &amount);

    if (amount < 0) {
        printf("Amount cannot be negative.\n");
        return;
    }

    newEntry.amount = amount;

    // Reallocate and append
    Entry *temp = realloc(*entries, (*count + 1) * sizeof(Entry));
    if (!temp) {
        printf("Memory allocation failed.\n");
        return;
    }

    *entries = temp;
    (*entries)[*count] = newEntry;
    (*count)++;

    printf("Entry added successfully with ID: %d\n", newEntry.id);
}


//option 5
void modifyEntry(Entry *entries, int count) {
    int id;
    char input[100];

    printf("Enter ID of entry to modify: ");
    fgets(input, sizeof(input), stdin);
    sscanf(input, "%d", &id);

    int index = -1;
    for (int i = 0; i < count; i++) {
        if (entries[i].id == id) {
            index = i;
            break;
        }
    }

    if (index == -1) {
        printf("Entry with ID %d not found.\n", id);
        return;
    }

    Entry *e = &entries[index];
    printf("\nCurrent Details:\n");
    printf("ID: %d\n", e->id);
    printf("Date: %s\n", e->date);
    printf("Type: %s\n", e->type);
    printf("Category: %s\n", e->category);
    printf("Description: %s\n", e->description);
    printf("Amount: $%.2f\n", e->amount);

    printf("\nWhat would you like to modify?\n");
    printf("1. Date\n");
    printf("2. Amount\n");
    printf("Choice: ");
    fgets(input, sizeof(input), stdin);

    int choice;
    sscanf(input, "%d", &choice);

    if (choice == 1) {
        printf("Enter new date (YYYY-MM-DD): ");
        fgets(e->date, sizeof(e->date), stdin);
        e->date[strcspn(e->date, "\n")] = 0;
        printf("Entry Date updated successfully.\n");
    } else if (choice == 2) {
        float newAmount;
        printf("Enter new amount: $");
        fgets(input, sizeof(input), stdin);
        sscanf(input, "%f", &newAmount);

        if (newAmount < 0) {
            printf("Amount cannot be negative.\n");
            return;
        }

        e->amount = newAmount;
        printf("Entry Amount updated successfully.\n");
    } else {
        printf("Invalid choice.\n");
    }
}


//option 6
void filterByMonth(Entry *entries, int count) {
    int year, month;
    char input[100];

    printf("Enter year (YYYY): ");
    fgets(input, sizeof(input), stdin);
    sscanf(input, "%d", &year);

    printf("Enter month (1-12): ");
    fgets(input, sizeof(input), stdin);
    sscanf(input, "%d", &month);

    if (month < 1 || month > 12) {
        printf("Invalid month.\n");
        return;
    }

    printf("\nEntries for %04d-%02d:\n\n", year, month);
    printf("%-6s %-12s %-10s %-12s %-20s %-10s\n",
           "ID", "Date", "Type", "Category", "Description", "Amount");
    printf("---------------------------------------------------------------\n");

    char filterPrefix[8];
    snprintf(filterPrefix, sizeof(filterPrefix), "%04d-%02d", year, month);

    int found = 0;
    for (int i = 0; i < count; i++) {
        if (strncmp(entries[i].date, filterPrefix, 7) == 0) {
            printf("%-6d %-12s %-10s %-12s %-20s $%-.2f\n",
                   entries[i].id,
                   entries[i].date,
                   entries[i].type,
                   entries[i].category,
                   entries[i].description,
                   entries[i].amount);
            found = 1;
        }
    }

    if (!found) {
        printf("No entries found for that month.\n");
    }
}


//option 8
void showIncomeBarChart(Entry *entries, int count) {
    float active = 0, passive = 0, other = 0;

    for (int i = 0; i < count; i++) {
        if (strcmp(entries[i].type, "income") == 0) {
            if (strcmp(entries[i].category, "Active") == 0)
                active += entries[i].amount;
            else if (strcmp(entries[i].category, "Passive") == 0)
                passive += entries[i].amount;
            else
                other += entries[i].amount;
        }
    }

    printf("\nIncome Distribution Chart (each * = $100)\n");
    printf("=========================================\n");

    printf("Active   : ");
    for (int i = 0; i < active / 100; i++) printf("*");
    printf(" ($%.2f)\n", active);

    printf("Passive  : ");
    for (int i = 0; i < passive / 100; i++) printf("*");
    printf(" ($%.2f)\n", passive);

    printf("Other    : ");
    for (int i = 0; i < other / 100; i++) printf("*");
    printf(" ($%.2f)\n", other);

    printf("=========================================\n");
}



