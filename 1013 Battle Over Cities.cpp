#include<bits/stdc++.h>
using namespace std;

int n, m ,k;
vector<int> G[1005];
bool vis[1005];

void DFS(int v){
    for (int i=0; i<(int)G[v].size(); i++){
        if (not vis[G[v][i]]){
            vis[G[v][i]] = 1;
            DFS(G[v][i]);
        }
    }
}

int main(){
    cin >> n >> m >> k;
    int i, j;
    
    for (i=0; i<m; i++){
        int a, b;
        cin >> a >> b;
        G[a].push_back(b);
        G[b].push_back(a);
    }
    
    for (i=0; i<k; i++){
        int v, comp=0;
        cin >> v;
        fill(vis, vis+1005, 0);
        vis[v] = 1;
        
        for (j=1; j<=n; j++){
            if (not vis[j]){
                comp += 1;
                DFS(j);
            }
        }
        
        cout << comp-1 << endl;
    }
    
    return 0;
}
