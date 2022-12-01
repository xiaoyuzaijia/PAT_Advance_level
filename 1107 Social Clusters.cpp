#include<bits/stdc++.h>
using namespace std;

int n, comp_n=0;
bool vis[2005];
vector<int> G[2005];
vector<int> comp;

void DFS(int v){
    int i;
    
    vis[v] = 1;
    if (v < 1000) comp_n += 1;
    for (i=0; i<(int)G[v].size(); i++){
        if (not vis[G[v][i]]) DFS(G[v][i]);
    }
}

int main(){
    cin >> n;
    int i, j;
    
    for (i=0; i<n; i++){
        int k, v;
        scanf("%d: ", &k);
        for (j=0; j<k; j++){
            cin >> v;
            v += 1000;
            G[i].push_back(v);
            G[v].push_back(i);
        }
    }
    
    for (i=0; i<n; i++){
        if (not vis[i]){
            comp_n = 0;
            DFS(i);
            comp.push_back(comp_n);
        }
    }
    
    cout << comp.size() << endl;
    sort(comp.begin(), comp.end());
    for (i=(int)comp.size()-1; i>0; i--){
        cout << comp[i] << ' ';
    }
    cout << comp[i] << endl;
    
    return 0;
}
