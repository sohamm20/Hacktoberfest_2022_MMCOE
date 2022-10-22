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
#include < iostream >
  using namespace std;

void bubbleSort(int a[]) {
  for (int i = 0; i < 5; i++) {
    for (int j = 0; j < (5 - i - 1); j++) {
      if (a[j] > a[j + 1]) {
        int temp = a[j];
        a[j] = a[j + 1];
        a[j + 1] = temp;
      }
    }
  }
}

int main() {
  int myarray[5];
  int size;
  cout << "Enter 5 integers in any order: " << endl;
  for (int i = 0; i < 5; i++) {
    cin >> myarray[i];
  }
  cout << "Before Sorting" << endl;
  for (int i = 0; i < 5; i++) {
    cout << myarray[i] << " ";
  }

  bubbleSort(myarray); // sorting

  cout << endl << "After Sorting" << endl;
  for (int i = 0; i < 5; i++) {
    cout << myarray[i] << " ";
  }

  return 0;
}
