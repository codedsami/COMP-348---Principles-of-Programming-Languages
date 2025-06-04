#ifndef ORDERING_H
#define ORDERING_H

#include "data.h"

int compareByID(const void *a, const void *b);
int compareByDate(const void *a, const void *b);
int compareByAmount(const void *a, const void *b);
int compareByDescription(const void *a, const void *b);

#endif
