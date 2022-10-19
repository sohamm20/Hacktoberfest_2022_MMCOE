#include <bits/stdc++.h>
using namespace std;

// Linearly search x in arr[]. If x is present then return
// its location, otherwise return -1
int search(int arr[], int n, int x)
{
	int i;
	for (i = 0; i < n; i++)
		if (arr[i] == x)
			return i;
	return -1;
}

// Driver code
int main()
{
    int n;
    cout<<"Enter Number of ele in array: ";
    cin>>n;
    
	int arr[n];
	cout<<"Start Entering elements of array\n";
	for(int i=0;i<n;i++){
	    cin>>arr[i];
	  
	}
	int z = sizeof(arr) / sizeof(arr[0]);
	int x ;
	cout<<"Enter number to be searched: ";
	cin>>x;

	int index = search(arr, z, x);
	if (index == -1)
		cout << "Element is not present in the array";
	else
		cout << "Element found at position " << index;

	return 0;
}
