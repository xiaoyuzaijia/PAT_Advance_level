#include<iostream>
#include<stack>
#include<queue>
using namespace std;

int n, k;
unsigned int m;

bool check(queue<int> q){
    int i;
    stack<int> in_s;
    stack<int> s;
    
    for (i=n; i>=1; i--){
        in_s.push(i);
    }
    
    while (!q.empty()){
        if ((!s.empty()) && (s.top() == q.front())){
            s.pop();
            q.pop();
        }
        else if (!in_s.empty()){
            s.push(in_s.top());
            in_s.pop();
            if (s.size() > m){
                return false;
            }
        }
        else if (in_s.empty()){
            return false;
        }
    }
    return true;
}

int main(){
    int i, j;
    cin>>m>>n>>k;
    
    for (i=0; i<k; i++){
        queue<int> q;
        for (j=0; j<n; j++){
            int x;
            cin>>x;
            q.push(x);
        }
        if (check(q)){
            cout<<"YES"<<endl;
        }
        else {
            cout<<"NO"<<endl;
        }
    }
    
    return 0;
}