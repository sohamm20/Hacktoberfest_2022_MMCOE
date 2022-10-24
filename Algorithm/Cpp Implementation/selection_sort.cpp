#include <bits/stdc++.h>
using namespace std;

void swapElements(int *xp, int *yp)
{
    int temp = *xp;
    *xp = *yp;
    *yp = temp;
}

void selectionSort(int arr[], int n)
{
    int min;

    for (int i = 0; i < n - 1; i++)
    {

        min = i;
        for (int j = i + 1; j < n; j++)
            if (arr[j] < arr[min])
                min = j;

        if (min != i)
            swapElements(&arr[min], &arr[i]);
    }
}

void printSortedArray(int arr[], int size)
{
    int i;
    for (i = 0; i < size; i++)
        cout << arr[i] << " ";
    cout << endl;
}

int main()
{
    int size;

    cout << "Enter the size: ";
    cin >> size;

    int arr[size];

    cout << "Enter the elements: ";

    for (int i = 0; i < size; i++)
    {
        cin >> arr[i];
    }
    cout << "Before Sorting: ";

    for (int i = 0; i < size; i++)
    {
        cout << arr[i] << "\t";
    }

    selectionSort(arr, size);

    cout << endl;

    cout << "After Sorting: ";
    for (int i = 0; i < size; i++)
    {
        cout << arr[i] << "\t";
    }

    return 0;
}
