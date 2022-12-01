#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

typedef long long int LL;
LL n, p;

LL f(LL M, LL m){
    return M - m*p;
}

int main(){
    cin >> n >> p;
    int i, j, l, r, maxn=1, mid;
    vector<LL> a(n);
    
    for (i=0; i<n; i++){
        cin >> a[i];
    }
    
    sort(a.begin(), a.end());
    a.push_back(1e9+1);
    
    for (i=0; i<n; i++){
        l = i;
        r = n;
        while (l<r){
            mid = (l+r)/2;
            if (f(a[mid], a[i]) > 0) r = mid;
            else l = mid + 1;
        }
        if (maxn < l-i) maxn = l-i;
    }
    
    cout << maxn << endl;
    
    return 0;
}