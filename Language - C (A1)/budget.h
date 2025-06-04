#ifndef BUDGET_H
#define BUDGET_H

#include "data.h"

void displayAllEntries(Entry *entries, int count);
void showExpenseDistribution(Entry *entries, int count);
void sortEntries(Entry *entries, int count);
void addEntry(Entry **entries, int *count);
void modifyEntry(Entry *entries, int count);
void filterByMonth(Entry *entries, int count);
void showIncomeBarChart(Entry *entries, int count);


#endif
