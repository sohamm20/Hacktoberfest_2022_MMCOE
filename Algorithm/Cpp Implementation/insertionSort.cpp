/* 
  Insertion Sort Algorithm –
      declare variables – i, key, j
      loop : i = 1 to n – 1 // outer loop
        key = a[i] //pick the next element
        j = i – j; // decrement j value
        loop : (j>=0 && a[j]>key) // inner loop
          arr[j+1] = arr[j]
          j = j – 1
        end loop // outer loop
        arr[j+1] = key
        end loop // outer loop
*/


#include <iostream>
  using namespace std;

void insertionSort(int arr[], int n) {
  int key;
  int j = 0;
  for (int i = 1; i < n; i++) {
    key = arr[i];
    j = i - 1;
    while (j >= 0 && arr[j] > key) {
      arr[j + 1] = arr[j];
      j = j - 1;
    }
    arr[j + 1] = key;
  }

}

int main() {
  int n;
  cout<<"Enter the size of array:- "; 
  cin>>n; 
  
  int arr[n];
  
  cout << "Enter the elements of array:- " << endl;
  for (int i = 0; i < n; i++) {
    cin >> arr[i];
  }

  cout << "Before Sorting it looked like: ";
  for (int i = 0; i < n; i++) {
    cout << arr[i] << "\t";
  }

  insertionSort(arr , n);

  cout << endl << "After Sorting it looks like:- ";
  for (int i = 0; i < n; i++) {
    cout << arr[i] << "\t";
  }

  return 0;
}
