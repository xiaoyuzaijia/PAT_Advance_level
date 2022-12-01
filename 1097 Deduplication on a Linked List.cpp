#include<bits/stdc++.h>
using namespace std;

struct Node{
    int add, v, next;
    Node(){}
    Node(int __add, int __v, int __next){
        add = __add;
        v = __v;
        next = __next;
    }
} a[100005];

int h, n;
vector<Node> l;
vector<Node> rl;
int hash_[10005];

void out_l(vector<Node> l){
    int i;
    
    if (l.empty()) return;
    
    for (i=0; i<(int)l.size()-1; i++){
        printf("%05d %d %05d\n", l[i].add, l[i].v, l[i+1].add);
    }
    
    printf("%05d %d -1\n", l[i].add, l[i].v);
}

int main(){
    cin >> h >> n;
    int i;
    
    for (i=0; i<n; i++){
        int add, v, next;
        cin >> add >> v >> next;
        a[add] = Node(add, v, next);
        
    }
    
    i = h;
    while (i != -1){
        hash_[abs(a[i].v)] += 1;
        if (hash_[abs(a[i].v)] == 1) l.push_back(a[i]);
        else rl.push_back(a[i]);
        i = a[i].next;
    }
    
    out_l(l);
    out_l(rl);
    
    return 0;
}