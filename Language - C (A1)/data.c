#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "data.h"

#define MAX_LINE_LEN 256

int loadEntries(const char *filename, Entry **entries, int *count) {
    FILE *file = fopen(filename, "r");
    if (!file) {
        fprintf(stderr, "Error: could not open %s\n", filename);
        return 0;
    }

    Entry *arr = NULL;
    int capacity = 10;
    int size = 0;
    arr = malloc(capacity * sizeof(Entry));
    if (!arr) {
        fprintf(stderr, "Memory allocation failed\n");
        fclose(file);
        return 0;
    }

    char line[MAX_LINE_LEN];
    while (fgets(line, sizeof(line), file)) {
        if (size >= capacity) {
            capacity *= 2;
            Entry *temp = realloc(arr, capacity * sizeof(Entry));
            if (!temp) {
                fprintf(stderr, "Realloc failed\n");
                free(arr);
                fclose(file);
                return 0;
            }
            arr = temp;
        }

        // Remove newline
        line[strcspn(line, "\n")] = 0;

        // Parse the line
        char *token = strtok(line, "|");
        if (!token) continue;
        arr[size].id = atoi(token);

        token = strtok(NULL, "|");
        if (!token) continue;
        strncpy(arr[size].date, token, sizeof(arr[size].date));

        token = strtok(NULL, "|");
        if (!token) continue;
        strncpy(arr[size].type, token, sizeof(arr[size].type));

        token = strtok(NULL, "|");
        if (!token) continue;
        strncpy(arr[size].category, token, sizeof(arr[size].category));

        token = strtok(NULL, "|");
        if (!token) continue;
        strncpy(arr[size].description, token, sizeof(arr[size].description));

        token = strtok(NULL, "|");
        if (!token) continue;
        arr[size].amount = strtof(token, NULL);

        size++;
    }

    fclose(file);
    *entries = arr;
    *count = size;
    return 1;
}
