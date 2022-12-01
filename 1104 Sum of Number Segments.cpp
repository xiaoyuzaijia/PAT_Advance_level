#include<bits/stdc++.h>
using namespace std;

int n;
double a[100005];
double dp[100005];
long long su;

int main(){
    cin >> n;
    int i;
    
    for (i=0; i<n; i++){
        cin >> a[i];
        a[i] *= 1000.0;
    }
    
//     sort(a, a+n);
    
    for (i=n-1; i>=0; i--){
        dp[i] = (long long)(dp[i+1] + (n-i)*a[i]);
        su += (long long)dp[i];
    }
    
    printf("%.2f\n", su/1000.0);
    
    return 0;
}
