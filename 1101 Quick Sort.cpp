#include<bits/stdc++.h>
using namespace std;

int n;
int a[100005];
bool is_piv[100005];

int main(){
    cin >> n;
    int i;
    memset(is_piv, 1, sizeof(is_piv));
    
    for (i=0; i<n; i++){
        cin >> a[i];
    }
    
    int max_e = -1;
    for (i=0; i<n; i++){
        if (max_e < a[i]){
            max_e = a[i];
        }
        else is_piv[i] = 0;
    }
    
    int min_e = 1e9+5;
    for (i=n-1; i>=0; i--){
        if (min_e > a[i]){
            min_e = a[i];
        }
        else is_piv[i] = 0;
    }
    
    int cnt=0;
    vector<int> piv;
    for (i=0; i<n; i++){
        if (is_piv[i] == 1){
            cnt++;
            piv.push_back(a[i]);
        }
    }
    cout << cnt << endl;
    
    if (cnt == 0){
        cout << endl;
        return 0;
    }
    
    sort(piv.begin(), piv.end());     // 按递增顺序输出所有的中枢
    for (i=0; i<(int)piv.size()-1; i++){
        cout << piv[i] << ' ';
    }
    cout << piv[i] << endl;
    
    return 0;
}
