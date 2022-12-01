#include<iostream>
#include<cstring>
#include<cmath>
using namespace std;

int m, n;
int h[10009];


bool is_prime(int n){
    if (n < 2) return false;
    else if (n == 2) return true;
    else if (n % 2 == 0) return false;
    else {
        for (int i=3; i*i<=n; i+=2){
            if (n % i == 0) return false;
        }
        return true;
    }
}

int hashv(int n){
    int fv, v, i=1;
    
    v = n % m;
    fv = v;
    while (h[v] != -1){
        v = (fv + i * i) % m;
        if (v == fv) return -1;
        i++;
    }
    return v;
}

int main(){
    cin >> m >> n;
    int i;
    memset(h, -1, 10009*sizeof(int));
    
    while (true){
        if (is_prime(m)) break;
        m++;
    }
    
    int x;
    for (i=0; i<n-1; i++){
        cin >> x;
        if (hashv(x) != -1){
            cout << hashv(x) << ' ';
            h[hashv(x)] = x;
        }
        else {
            cout << "- ";
        }
    }
    
    cin >> x;
    if (hashv(x) != -1){
        cout << hashv(x) << endl;
        h[hashv(x)] = x;
    }
    else {
        cout << "-" << endl;
    }
    
    return 0;
}