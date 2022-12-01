#include<iostream>
#include<algorithm>
using namespace std;
int N, M;
int a[100005];

int two_find(int l, int r){
    int i, m;
    
    i = l - 1;      // 第i个就是l-1,记录一下i方便计算给的钱
    while (l <= r){
        m = (l + r) / 2;
        if (a[i] + a[m] == M){
            return m;
        }
        else if (a[i] + a[m] < M){
            l = m + 1;
        }
        else {
            r = m - 1;
        }
    }
    return -1;
}

int main(){
    int i, j;
    cin>>N>>M;
    for (i=0; i<N; i++){
        cin>>a[i];
    }
    
    sort(a, a+N);
    
    for (i=0; i<N; i++){
        j = two_find(i+1, N-1);  // 从i+1开始找,因为一个coin不能用两次
        if (j != -1){
            cout<<a[i]<<' '<<a[j]<<endl;
            return 0;
        }
    }
    
    cout<<"No Solution"<<endl;
    
    return 0;
}