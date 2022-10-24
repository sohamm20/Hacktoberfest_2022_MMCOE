#include <bits/stdc++.h>
using namespace std;

void swap(int *xp, int *yp)
{
    int temp = *xp;
    *xp = *yp;
    *yp = temp;
}

void selectionSort(int arr[], int n)
{
    int i, j, min_idx;

    // One by one move boundary of
    // unsorted subarray
    for (i = 0; i < n - 1; i++)
    {

        min_idx = i;
        for (j = i + 1; j < n; j++)
            if (arr[j] < arr[min_idx])
                min_idx = j;

        if (min_idx != i)
            swap(&arr[min_idx], &arr[i]);
    }
}

void printArray(int arr[], int size)
{
    int i;
    for (i = 0; i < size; i++)
        cout << arr[i] << " ";
    cout << endl;
}

int main()
{
    int size;

    cout << "Enter the size of array:- ";
    cin >> size;

    int arr[size];

    cout << "Enter the elements of array:- ";

    for (int i = 0; i < size; i++)
    {
        cin >> arr[i];
    }
    cout << "Before Sorting it looked like:- ";

    for (int i = 0; i < size; i++)
    {
        cout << arr[i] << "\t";
    }

    selectionSort(arr, size); // sorting

    cout << endl;

    cout << endl
         << "After Sorting it looks like:- ";
    for (int i = 0; i < size; i++)
    {
        cout << arr[i] << "\t";
    }

    return 0;
}
