#include <iostream>
using namespace std;
 
int main()
{
    int n;
    cout<<"Enter the number: ";
    cin>>n;
    cout << "The total number of set bits in " << n << " is "
         << __builtin_popcount (n) << endl;
 
    return 0;
}
