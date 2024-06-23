
CFLAGS ?= -O3
merge:
	gcc -c $(CFLAGS) mergesort.c -o merge
main_merge:
	gcc $(CFLAGS) merge main.c -o mergesort

bubble:
	gcc -c $(CFLAGS) bubblesort.c -o bubble
main_bubble:
	gcc $(CFLAGS) -D USE_BUBBLE_SORT bubble main.c -o bubblesort

all_merge:
	gcc -c $(CFLAGS) mergesort.c -o merge
	gcc -O3 merge main.c -o mergesort

all_bubble:
	gcc -c $(CFLAGS) bubblesort.c -o bubble
	gcc -O3 -D USE_BUBBLE_SORT bubble main.c -o bubblesort


