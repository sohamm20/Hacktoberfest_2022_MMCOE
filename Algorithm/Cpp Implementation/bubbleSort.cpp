/* 
  Bubble Sort Algorithm –
    declare variables – i, j
    loop : i = 0 to n – 1 // outer loop
      loop : j = 0 to n -i- 1 // inner loop
        if ( a[j]>a[j+1] ) then
          swap a[j] & a[j+1]
      end loop // inner loop
    end loop // outer loop
*/ 
#include <iostream>
  using namespace std;

void bubbleSort(int a[], int n) {
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < (n - i - 1); j++) {
      if (a[j] > a[j + 1]) {
        int temp = a[j];
        a[j] = a[j + 1];
        a[j + 1] = temp;
      }
    }
  }
}

int main() {
  int size;
  
  cout<<"Enter the size of array:- ";
  cin>> size; 
  
  int arr[size]; 
  
  cout << "Enter the elements of array:- "; 
  
  for (int i = 0; i < size; i++) {
    cin >> arr[i];
  }
  cout << "Before Sorting it looked like:- ";
  
  for (int i = 0; i < size; i++) {
    cout << arr[i] << "\t";
  }

  bubbleSort(arr,size); // sorting
  
	cout<<endl; 
	
  cout << endl << "After Sorting it looks like:- ";
  for (int i = 0; i < size; i++) {
    cout << arr[i] << "\t";
  }

  return 0;
}
