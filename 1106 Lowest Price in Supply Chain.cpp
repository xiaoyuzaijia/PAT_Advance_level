#include<bits/stdc++.h>
using namespace std;

int n, min_n;
double p, r, min_p=1e10+1;
vector<int> G[100005];

void BFS(int s){
    int i, v, w, last, l_last, level;
    queue<int> q;
    q.push(s);
    
    level = 0;
    last = s;
    l_last = s;
    while (not q.empty()){
        v = q.front();
        q.pop();
        if (G[v].empty()){
            if (min_p > p*pow(1+r, level)){
                min_p = p*pow(1+r, level);
                min_n = 1;
            }
            else if (min_p == p*pow(1+r, level)){
                min_n++;
            }
        }
        for (i=0; i<(int)G[v].size(); i++){
            q.push(G[v][i]);
            last = G[v][i];
        }
        
        if (v == l_last){
            level += 1;
            l_last = last;
        }
    }
    
    
}

int main(){
    cin >> n >> p >> r;
    r /= 100;
    int i, j;
    
    for (i=0; i<n; i++){
        int v, k;
        cin >> k;
        for (j=0; j<k; j++){
            cin >> v;
            G[i].push_back(v);
        }
    }
    
    BFS(0);
    
    printf("%.4f %d\n", min_p, min_n);
    
    return 0;
}