#include<cstdio>
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

struct Node{
    int add;
    int key;
    int next;
} node[100005];

int n, head;

bool cmp(Node a, Node b){
    return (a.key < b.key);
}

int main(){
    int i;
    cin>>n>>head;
    
    if (head == -1){
        cout<<0<<' '<<-1<<endl;
        return 0;
    }
    
    for (i=0; i<n; i++){
        int add, key, next;
        cin>>add>>key>>next;
        node[add].add = add;
        node[add].key = key;
        node[add].next = next;
    }
    
    vector<Node> l;
    int current, count;
    current = head;
    count = 0;
    while (current != -1){
        l.push_back(node[current]);
        current = node[current].next;
        count += 1;
    }
    
    
    sort(l.begin(), l.end(), cmp);
    
    printf("%d %05d\n", count, l[0].add);
    for (i=0; i<count-1; i++){
        printf("%05d %d %05d\n", l[i].add, l[i].key, l[i+1].add);
    }
    printf("%05d %d -1\n", l[count-1].add, l[count-1].key);
    
    return 0;
}