/*
Author:       Jordan Ringenberg
Last Updated: Sept. 29, 2021

	This code file contains 5 sorting methods:

	1)	Bubble Sort
	2)	Insertion Sort
	3)	Selection Sort
	4)	Quick Sort
	5)	Merge Sort

	There is also a timing method in order to compare the performance of these
	sorting algorithms on using three different kinds of lists:

	1)	All elements already in sorted (ascending) order
	2)	All elements in reverse sorted (descending) order
	3)	All elements in random order

	This is a supplemental file to be used as basis for writing your code, and
	comparing the timing results from these algorithms in C++ and Python
*/

#include <iostream>
#include <iomanip>
#include <string>
#include <chrono>
#include <iterator>

using namespace std;

//Timing/clock logic derived from Martin G's StackOverflow answer:
//https://stackoverflow.com/questions/3220477/how-to-use-clock-in-c
typedef std::chrono::high_resolution_clock Clock;

//////////////////////////////////////////////////////////////
//Utility Functions
//////////////////////////////////////////////////////////////
void swap(int &i, int &j) {
	int t = i;
	i = j;
	j = t;
}

void printArr(int a[], int numElements) {
	for (int i = 0; i < numElements; i++) {
		cout << a[i] << " ";
	}
	cout << endl;
}

//////////////////////////////////////////////////////////////
//Bubble Sort
//////////////////////////////////////////////////////////////
void bubbleSort(int arr[], int startIndex, int lastIndex) {
	bool didSwap = true;

	while (didSwap) {

		didSwap = false;

		for (int i = startIndex + 1; i <= lastIndex; i++) {

			if (arr[i - 1] > arr[i]) {
				swap(arr[i - 1], arr[i]);
				didSwap = true;
			}
		}
	}
}
//////////////////////////////////////////////////////////////
//Selection Sort
//////////////////////////////////////////////////////////////
int findLargest(int arr[], int startIndex, int stopIndex) {
	int largestIndex = startIndex;

	for (int i = startIndex; i <= stopIndex; i++) {
		if (arr[i] > arr[largestIndex]) {
			largestIndex = i;
		}
	}
	return largestIndex;
}
void selSort(int arr[], int startIndex, int lastIndex) {
	int largestIndex = 0;

	for (int i = lastIndex; i > startIndex; i--) {

		//find largest item in unsorted portion of array
		largestIndex = findLargest(arr, startIndex, i);

		//swap largest value into proper order
		swap(arr[largestIndex], arr[i]);
	}
}

//////////////////////////////////////////////////////////////
//Insertion Sort
//////////////////////////////////////////////////////////////
void insSort(int arr[], int startIndex, int lastIndex) {

	int loc = 0,
		key = 0;

	//the list will become sorted one correct insertion per pass
	for (int i = startIndex + 1; i <= lastIndex; i++) {

		//key will be the first element in the non-sorted list portion
		key = arr[i];
		loc = i - 1;

		//find the location within the sorted portion to place key
		//move all items greater than key one item forward in array
		while ((loc >= 0) && (arr[loc] > key)) {
			arr[loc + 1] = arr[loc];
			loc--;
		}

		//insert item in appropriate spot
		arr[loc + 1] = key;
	}
}

//////////////////////////////////////////////////////////////
//Quicksort
//////////////////////////////////////////////////////////////
int partition(int arr[], int left, int right) {
	int p = left + rand() % (right - left + 1);
	int pivot = arr[p];
	int l = left + 1;
	int r = right;

	swap(arr[p], arr[left]);

	while (l < r) {
		while (l < r && arr[l] <= pivot) {
			l++;
		}
		while (arr[r] > pivot) {
			r--;
		}
		if (l < r && arr[l] > arr[r]) {
			swap(arr[l], arr[r]);
		}
	}
	if (pivot > arr[r]) {
		swap(arr[r], arr[left]);
	}

	return r;
}

void quickSort(int arr[], int left, int right) {
	int pivot;
	if (left < right) {
		pivot = partition(arr, left, right);
		quickSort(arr, left, pivot - 1);
		quickSort(arr, pivot + 1, right);
	}
}

//////////////////////////////////////////////////////////////
//Merge Sort
//////////////////////////////////////////////////////////////
void merge(int arr[], int left, int splitPos, int right) {
	int  len = right - left + 1;
	int* arrB = new int[len];
	int rStart = splitPos - left + 1;

	for (int i = 0; i < len; i++) {
		arrB[i] = arr[left + i];
	}

	for (int i = left, l = 0, r = rStart; i <= right; i++) {
		if (r >= len || (l < rStart && arrB[l] <= arrB[r])) {
			arr[i] = arrB[l];
			l++;
		}
		else {
			arr[i] = arrB[r];
			r++;
		}
	}

	delete[] arrB;
}

void mergeSort(int arr[], int left, int right) {
	int splitpos;
	if (left < right) {
		// Partition the array into two subarrays, 
		//sort these subarrays recursively and then 
		//merge them into a correctly sorted array.
		splitpos = (left + right) / 2;
		mergeSort(arr, left, splitpos);
		mergeSort(arr, splitpos + 1, right);
		merge(arr, left, splitpos, right);
	}
}

//////////////////////////////////////////////////////////////
//Timing and Analysis Functions
// (Note the function pointer as the first parameter - this
// takes one of the sorting functions as a parameter to then
// run analysis on)
//////////////////////////////////////////////////////////////
void timeAlg(void(*sortAlg)(int[], int, int), int arr[], int startIndex, int endIndex, string analysisName) {
	//Timing/clock logic derived from Martin G's StackOverflow answer:
	//https://stackoverflow.com/questions/3220477/how-to-use-clock-in-c

	auto startTime = Clock::now();
	//printArr(arr, endIndex + 1);
	sortAlg(arr, startIndex, endIndex);
	//printArr(arr, endIndex + 1);
	auto finishTime = Clock::now();

	auto duration = finishTime - startTime;

	auto timeElapsed_inMilliseconds = chrono::duration_cast<std::chrono::microseconds> (duration).count() / 1000.0;

	cout << setprecision(2) << fixed;
	cout << analysisName << " time to sort (milliseconds): " << timeElapsed_inMilliseconds << endl;
}

void analyzeAlg(void(*sortAlg)(int[], int, int), int asc_arr[], int desc_arr[], int rnd_arr[], const int ARRSIZE, string sortName) {
	int* asc_cpy = new int[ARRSIZE];
	int* desc_cpy = new int[ARRSIZE];
	int* rnd_cpy = new int[ARRSIZE];

	//copy Original Arrays into ones for testing
	std::copy(asc_arr, asc_arr + ARRSIZE, asc_cpy);
	std::copy(desc_arr, desc_arr + ARRSIZE, desc_cpy);
	std::copy(rnd_arr, rnd_arr + ARRSIZE, rnd_cpy);

	//run sorting and timing
	timeAlg(sortAlg, asc_cpy, 0, ARRSIZE - 1, sortName + " on ascending array :");
	timeAlg(sortAlg, desc_cpy, 0, ARRSIZE - 1, sortName + " on descending array :");
	timeAlg(sortAlg, rnd_cpy, 0, ARRSIZE - 1, sortName + " on randomized array :");

	cout << endl;

	delete[] asc_cpy;
	delete[] desc_cpy;
	delete[] rnd_cpy;
}

//////////////////////////////////////////////////////////////
//Main set to run tests
//////////////////////////////////////////////////////////////
int main() {
	srand(unsigned int(time(NULL)));

	const int ARRSIZE = 20000;

	//Create the different arrays
	int ascendingArr[ARRSIZE];
	int descendingArr[ARRSIZE];
	int randomArr[ARRSIZE];

	//Populate each array according to the order of data
	for (int i = 0; i < ARRSIZE; i++) {
		ascendingArr[i] = i;
		descendingArr[i] = ARRSIZE - i - 1;
		randomArr[i] = rand() % ARRSIZE;
	}

	analyzeAlg(bubbleSort, ascendingArr, descendingArr, randomArr, ARRSIZE, "Bubble sort");
	analyzeAlg(selSort, ascendingArr, descendingArr, randomArr, ARRSIZE, "Selection sort");
	analyzeAlg(insSort, ascendingArr, descendingArr, randomArr, ARRSIZE, "Insertion sort");
	analyzeAlg(quickSort, ascendingArr, descendingArr, randomArr, ARRSIZE, "Quick sort");
	analyzeAlg(mergeSort, ascendingArr, descendingArr, randomArr, ARRSIZE, "Merge sort");


	return 0;
}
