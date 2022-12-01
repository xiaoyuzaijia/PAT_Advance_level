#include<iostream>
#include<vector>
using namespace std;

int n;

bool is_prime(int n){
    int i;
    
    if (n == 2) return true;
    if (n % 2 == 0) return false;
    for (i=3; i*i<=n; i+=2){
        if (n % i == 0) return false;
    }
    return true;
}

int main(){
    int i;
    vector<int> v;
    cin >> n;
    
    cout << n << '=';
    
    if (n == 1){
        cout << 1 << endl;
        return 0;
    }
    
    while (n != 1){
        for (i=2; i<=n; i++){
            if (is_prime(i) && n%i == 0) break;
        }
        v.push_back(i);
        n /= i;
    }
    
    
    v.push_back(-1);
    
    int cnt = 1;
    for (i=0; i<((int)v.size()-1); i++){
        if (i >= 1 && v[i-1] != v[i]){
            cout << '*';
        }
        
        if (v[i] == v[i+1]){
            if (cnt == 1){
                cout << v[i];
            }
            cnt++;
        }
        else {
            if (cnt == 1){
                cout << v[i];
            }
            else {
                cout << '^' << cnt;
                cnt = 1;
            }
        }
    }
    
    cout << endl;
    
    return 0;
}