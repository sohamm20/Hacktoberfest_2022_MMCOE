// quick sort. 

/* also works on the lines of divide and conquer. 
here we decide one pivot element and keep it at its approrite place. 
we do partition of array using the pivot .
3 variables:- lower upper

*/

#include<iostream>
using namespace std; 

/* function of quick sort. */
/* while(lower<upper) {
	while(arr[lower],pivot)
		lower = lower - 1;
		
	while(arr[upper]>pivot) 
		upper = upper - 1;
		
	if(lower<upper) {
		temp = arr[lower];
		arr[lower]=arr[upper];
		arr[upper] = temp;
	}

}
*/ 

void quicksort(int number[25],int first,int last){

	int i, j, pivot, temp;
	
	if(first<last){
	
		pivot=first;
		
		i=first;
		
		j=last;
	
		while(i<j){
		
			while(number[i]<=number[pivot]&&i<last)
				i++;
			
			while(number[j]>number[pivot])
				j--;
			
			if(i<j){
				temp=number[i];
				number[i]=number[j];
				number[j]=temp;
			
			}
		}
	
		temp=number[pivot];
		number[pivot]=number[j];
		number[j]=temp;
		quicksort(number,first,j-1);
		quicksort(number,j+1,last);	
	}
} 

int main() {
	int arr[10] = {25, 63, 58, 14, 53, 12, 15, 26, 30, 13};
	quicksort(arr, 0, 9); 
	
	for(int i=0; i<10; i++) {
		cout<<arr[i]<<"\t";
	}
	return 0;
}
