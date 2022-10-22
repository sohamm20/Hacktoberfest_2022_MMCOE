// heap sort

/* 
left child = 2i +1;

right child = 2i + 2;

parent of i = (i-1)/2 ; 

heap is a data structure where we represent tree in array format. 

poperties:- 
1) complete binary tree. 
2) all nodes are greater than their children. (max heap)
3) all nodes are smaller than their children (min heap).

heapify function:- this function is the process of creating a heap out of a binary tree. 

*/
#include<iostream>
using namespace std; 
//heapify functipn

void heapify(int *arr, int n, int i) {
	int largest = i;
	int left = 2*i + 1;
	int right = 2*i +2;
	
	if((left<n) && (arr[left] > arr[largest])) 
		largest = left; 
		
	if((right < n) && (arr[right] > arr[largest]))
		largest = right; 
	
	if(i!=largest) {
		int temp = arr[i];
		arr[i] = arr[largest];
		arr[largest] = temp;
		
		heapify(arr,n,largest); // recurssion checking again agian to create a max heap. 
		
	}
}

void heapSort(int *arr, int n) {
	int i;
	// build max heap. 
	
	for(int i=n/2-1; i>=0; i--) {
		heapify(arr,n,i);
	} 
	
	for(i = n-1; i>=0; i--) {
		int temp = arr[0];
		arr[0] = arr[i];
		arr[i] = temp;
		
		heapify(arr, i, 0); 
	}
}

int main() {
	
	int arr[10] = {12,15, 85, 64, 924, 4654, 251, 314, 457, 967}; 
	heapSort(arr,10); 
	cout<<"Sorted order is as follows!"<<endl; 
	for(int i=0; i<10; i++) 
		cout<<arr[i]<<"\t";
		
	return 0;
}
