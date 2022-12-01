#include<cstdio>
#include<algorithm>
#include<iostream>
#include<cmath>
#include<cstring>
using namespace std;

int n, k, p;
int a[405], b[405];
int found=0;
int max_k=0, n_sum=0;

bool cmp(int a, int b){
    return a > b;
}

int k_sum(int index){
    int i, s=0;
    
    for (i=0; i<=index; i++) s += a[i];
    s += (k-1-index) * a[index];
    
    return s;
}


void gerne(int i, int index){
    if (index == k){
        if (n_sum == n && max_k < k_sum(k-1)){
            found = 1;
            max_k = k_sum(k-1);
            memcpy(b, a, sizeof(a));
        }
        return;
    }
    else {
        for (int j=i; j>0; j--){
            a[index] = j;
            n_sum += pow(j, p);
            if (n_sum <= n){
                gerne(j, index+1);
            }
            n_sum -= pow(j, p);
        }
    }
}

int main(){
    cin >> n >> k >> p;
    int i;
    
    gerne((int)(log(n)/log(p))+1, 0);
    
    if (found <= 0){
        cout << "Impossible" << endl;
        return 0;
    }
    
    
    sort(b, b+k, cmp);
    printf("%d = ", n);
    for (i=0; i<k-1; i++){
        printf("%d^%d + ", b[i], p);
    }
    printf("%d^%d\n", b[i], p);
    
    return 0;
}