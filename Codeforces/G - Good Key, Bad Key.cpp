#include <bits/stdc++.h>
using namespace std;

vector<vector<long long>> dp(33, vector<long long> (100005, LLONG_MAX));

long long solve(vector<long long> &a, long long i, long long count, long long k, long long n){
	
	if (i > n - 1 || count > 32){
		return 0;
	}
	
	if (dp[count][i] != LLONG_MAX){
		return dp[count][i];
	}

	long long ans = max(solve(a, i + 1, count, k, n) + (a[i] >> count) - k, solve(a, i + 1, count + 1, k, n) + (a[i] >> (count + 1)));
	dp[count][i] = ans;
	return ans;
}


int main(){

	ios_base::sync_with_stdio(false);
    cin.tie(NULL);   

	long long t;
	cin >> t;
	while (t--){

		long long n, k;
		cin >> n >> k;

		for (auto &v: dp) {
		    std::fill(v.begin(), v.begin() + n + 2, LLONG_MAX);
		}

		vector<long long> a(n);
		for (long long i = 0; i < n; i++){
			cin >> a[i];
		}

		cout << solve(a, 0, 0, k, n) << endl;
		
	}
	return 0;

}
