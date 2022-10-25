#include <iostream>
using namespace std;

int main()
{
    // your code goes here
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        int a[100000];
        for (int i = 0; i < n; i++)
        {
            cin >> a[i];
        }
        int z = 0, o = 0;
        for (int i = 0; i < n; i++)
        {
            if (a[i] == 0)
            {
                z++;
            }
            else
            {
                o++;
            }
        }
        if (z >= o)
        {
            cout << o << endl;
        }
        else
        {
            int ans = z + (o - z) / 3;
            cout << ans << endl;
        }
    }
    return 0;
}