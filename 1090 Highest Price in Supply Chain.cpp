#include<iostream>
#include<cstdio>
#include<cmath>
#include<vector>
using namespace std;

int n;
double p, r;
vector<int> G[100005];
double P[100005];

void DFS(int v, int deep){
    int i;
    
    if (G[v].empty()){
        P[v] = p * pow(1+r, deep);
        return;
    }
    
    for (i=0; i<(int)G[v].size(); i++){
        DFS(G[v][i], deep+1);
    }
}

int main(){
    cin >> n >> p >> r;
    r /= 100;
    int i, v, w, cnt=0;
    
    for (v=1; v<=n; v++){
        cin >> w;
        G[w+1].push_back(v);
    }
    
    DFS(0, -1);
    
    double max_p=0.0;
    for (i=0; i<=n; i++){
        if (max_p < P[i]){
            max_p = P[i];
            cnt = 0;
        }
        if (max_p == P[i]) cnt++;
    }
    
    printf("%.2f %d\n", max_p, cnt);
    
    return 0;
}
