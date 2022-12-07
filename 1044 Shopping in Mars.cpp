#include<bits/stdc++.h>
using namespace std;

int n, m;
int a[100005];
int s[100005];
vector<pair<int ,int>> ans;

int main(){
    cin >> n >> m;
    int i, l=1, r=1;
    
    for (i=1; i<=n; i++) cin >> a[i];
    for (i=1; i<=n; i++) s[i] = s[i-1] + a[i];
    
    int min_big = 1e9;
    while (r<=n or (r==n and s[r]-s[l-1]>=m)){
        if (s[r]-s[l-1] > m){
            if (min_big > s[r]-s[l-1]) min_big = s[r]-s[l-1];
            l++;
        }
        else if (s[r]-s[l-1] < m){
            r++;
        }
        else {
            ans.push_back(make_pair(l, r));
            l++;
        }
    }
    
    if (not ans.empty()){
        for (i=0; i<(int)ans.size()-1; i++){
            cout << ans[i].first << '-' << ans[i].second << endl;
        }
        cout << ans[i].first << '-' << ans[i].second;
        return 0;
    }
    
    m = min_big;
    l = 1;
    r = 1;
    while (r<=n or (r==n and s[r]-s[l-1]>=m)){
        if (s[r]-s[l-1] > m){
            l++;
        }
        else if (s[r]-s[l-1] < m){
            r++;
        }
        else {
            ans.push_back(make_pair(l, r));
            l++;
        }
    }
    
    for (i=0; i<(int)ans.size()-1; i++){
            cout << ans[i].first << '-' << ans[i].second << endl;
        }
    cout << ans[i].first << '-' << ans[i].second;
    return 0;
}
