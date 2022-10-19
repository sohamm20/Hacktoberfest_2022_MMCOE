#include <iostream>
using namespace std;
 
int main()
{
    int n;
    cout<<"Enter the number: ";
    cin>>n;

    int ans = 0;

    for (int i = 0; i < 32; i++){
        if (1 << i & n){
            ans++;
        }
    }

    cout << "The total number of set bits in " << n << " is " << ans << endl;
 
    return 0;
}
