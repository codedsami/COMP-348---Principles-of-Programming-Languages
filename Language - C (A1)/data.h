#ifndef DATA_H
#define DATA_H

typedef struct {
    int id;
    char date[11];        // YYYY-MM-DD + '\0'
    char type[10];        // "income" or "expense"
    char category[20];    // "Needs", "Wants", etc.
    char description[101];
    float amount;
} Entry;

// Load entries from file
int loadEntries(const char *filename, Entry **entries, int *count);

#endif
