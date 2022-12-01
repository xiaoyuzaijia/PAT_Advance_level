#include<bits/stdc++.h>
using namespace std;

struct Node{
    int v, l, r;
    Node(){}
    Node(int __v, int __l, int __r){
        v = __v;
        l = __l;
        r = __r;
    }
} a[105];

int n;
vector<int> in_l;
vector<int> le_l;

void in_t(int i){
    if (i != -1){
        in_t(a[i].l);
        a[i].v = in_l[0];
        in_l.erase(in_l.begin());
        in_t(a[i].r);
    }
}

void le_t(int i){
    int root;
    queue<int> q;
    
    q.push(i);
    while (not q.empty()){
        root = q.front();
        q.pop();
        le_l.push_back(a[root].v);
        if (a[root].l != -1) q.push(a[root].l);
        if (a[root].r != -1) q.push(a[root].r);
    }
}

int main(){
    cin >> n;
    int i;
    
    for (i=0; i<n; i++){
        int l, r;
        cin >> l >> r;
        a[i] = Node(-1, l, r);
    }
    
    for (i=0; i<n; i++){
        int v;
        cin >> v;
        in_l.push_back(v);
    }
    
    sort(in_l.begin(), in_l.end());
    
    in_t(0);
    le_t(0);
    
    for (i=0; i<(int)le_l.size()-1; i++){
        cout << le_l[i] << ' ';
    }
    cout << le_l[i] << endl;
    
    return 0;
}