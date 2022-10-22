// Optimized bubble sort is basically a smarter version of bubble sort algorithm.
// Hence the algorithm is same as BubbleSort with a mechanism to determine whether the list/array DS is sorted or not after every iteration, which ensures that 
// the program only runs till the array/list is sorted.
//
// Optimized bubble sort is basically a smarter version of bubble sort algorithm.
// Hence the algorithm is same as BubbleSort with a mechanism to determine whether the list/array DS is sorted or not after every iteration, which ensures that 
// the program only runs till the array/list is sorted.
//
#include <iostream>
using namespace std;

void optimizedbubbleSort(int a[]) {
  int rounds = 0;
  for (int i = 0; i < 5; i++) {
    rounds++;
    int flag = false;
    for (int j = 0; j < (5 - i - 1); j++) {
      if (a[j] > a[j + 1]) {
        flag = true;
        int temp = a[j];
        a[j] = a[j + 1];
        a[j + 1] = temp;
      }
    }
    if (flag == false) {
      break;
    }
  }
  cout << "No of rounds : " << rounds << endl;
}

int main() {
	
  int n; 
  cout<<"Enter the size of array:- ";
  cin>>n; 
  
  int arr[n];
  cout << "Enter the elements of array:- ";
  for (int i=0; i<n; i++) {
    cin >> arr[i];
  }
  
  cout << "Before Sorting it looked like" << endl;
  for (int i=0 ; i<n ; i++) {
    cout << arr[i] << "\t";
  }
  cout<<endl;
  
  optimizedbubbleSort(arr); // sorting

  cout << "After Sorting it looks like:- " << endl;
  for (int i=0; i<n; i++) {
    cout << arr[i] << "\t";
  }

  return 0;
}
