#include <string.h>
#include "data.h"

int compareByID(const void *a, const void *b) {
    Entry *e1 = (Entry *)a;
    Entry *e2 = (Entry *)b;
    return e1->id - e2->id;
}

int compareByDate(const void *a, const void *b) {
    Entry *e1 = (Entry *)a;
    Entry *e2 = (Entry *)b;
    return strcmp(e1->date, e2->date);
}

int compareByAmount(const void *a, const void *b) {
    Entry *e1 = (Entry *)a;
    Entry *e2 = (Entry *)b;
    if (e1->amount < e2->amount) return -1;
    if (e1->amount > e2->amount) return 1;
    return 0;
}

int compareByDescription(const void *a, const void *b) {
    Entry *e1 = (Entry *)a;
    Entry *e2 = (Entry *)b;
    return strcmp(e1->description, e2->description);
}
