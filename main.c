#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "bubblesort.h"
#include "mergesort.h"

// Macro to choose sorting algorithm
//#define USE_BUBBLE_SORT // Set to 0 to use Merge Sort

void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <array_size>\n", argv[0]);
        return 1;
    }

    int n = atoi(argv[1]);
    int *arr = (int *)malloc(n * sizeof(int));

    // Seed for random number generation
    srand(time(0));

    // Initialize the array with random values
    for (int i = 0; i < n; i++) {
        arr[i] = rand() % 100; // Random numbers between 0 and 99
    }

    //printf("Given array is \n");
    //printArray(arr, n);

#ifdef USE_BUBBLE_SORT
    bubbleSort(arr, n);
#else
    mergeSort(arr, 0, n - 1);
#endif

    //printf("Sorted array is \n");
    //printArray(arr, n);

    free(arr);
    return 0;
}

