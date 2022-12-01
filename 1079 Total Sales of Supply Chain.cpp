#include<cstdio>
#include<iostream>
#include<vector>
#include<algorithm>
#include<cmath>
using namespace std;

int n;
double p, r, pro=0.0;
int c[100001] = {0};
vector<int> G[100001];

void DFS(int v, int deep){
    if (c[v] != 0){
        pro += p * pow(1+r, deep) * c[v];
        return;
    }
    for (int i=0; i<(int)G[v].size(); i++){
        DFS(G[v][i], deep+1);
    }
}

int main(){
    cin >> n >> p >> r;
    r /= 100;
    int v, w, i;
    
    for (v=0; v<n; v++){
        int out;
        cin >> out;
        if (out == 0) {
            int cus;
            cin >> cus;
            c[v] = cus;
        }
        for (i=0; i<out; i++){
            cin >> w;
            G[v].push_back(w);
        }
    }
    
    DFS(0, 0);
    
    printf("%.1f\n", pro);
    
    return 0;
}