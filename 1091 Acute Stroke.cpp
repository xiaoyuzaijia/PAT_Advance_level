#include<bits/stdc++.h>
#include<iostream>
using namespace std;

struct Node{
    int x, y, z;
    Node (){}
    Node (int __x, int __y, int __z){
        x = __x;
        y = __y;
        z = __z;
    }
};

int m, n, l, t, core_size;
bool g[60][1286][128];
bool vis[60][1286][128] = {0};

bool can_vis(int x, int y, int z){
    if (x<0 || x>=l || y<0 || y>=m || z<0 || z>=n) return false;
    else if (g[x][y][z] and not vis[x][y][z]) return true;
    else return false;
}

void BFS(int x, int y, int z){
    int X[] = {0, 0, 0, 0, 1, -1};
    int Y[] = {0, 0, 1, -1, 0, 0};
    int Z[] = {1, -1, 0, 0, 0, 0};
    int newx, newy, newz; 
    
    vis[x][y][z] = 1;
    core_size += 1;
    Node s(x, y, z);
    queue<Node> q;
    q.push(s);
    
    while (not q.empty()){
        Node v=q.front();
        q.pop();
        
        for (int i=0; i<6; i++){
            newx = v.x + X[i];
            newy = v.y + Y[i];
            newz = v.z + Z[i];
            if (can_vis(newx, newy, newz)){
                vis[newx][newy][newz] = 1;
                core_size += 1;
                q.push(Node(newx, newy, newz));
            }
        }
    }
}

int main(){
    cin >> m >> n >> l >> t;
    int x, y, z;
    
    for (x=0; x<l; x++){
        for (y=0; y<m; y++){
            for (z=0; z<n; z++) cin >> g[x][y][z];
        }
    }
    
    int total_size=0;
    for (x=0; x<l; x++){
        for (y=0; y<m; y++){
            for (z=0; z<n; z++){
                if (can_vis(x, y, z)){
                    core_size = 0;
                    BFS(x, y, z);
                    if (core_size >= t) total_size += core_size;
                }
            }
        }
    }
    
    cout << total_size << endl;
    
    return 0;
}