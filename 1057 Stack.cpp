#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;

int n;

int main(){
    int i;
    vector<int> s;
    cin >> n;
    
    for (i=0; i<n; i++){
        string op;
        cin >> op;
        
        if (op == "Push"){
            int key;
            cin >> key;
            s.push_back(key);
        }
        else if (op == "Pop"){
            if (s.empty()) cout << "Invalid" << endl;
            else {
                cout << *(s.end()-1) << endl;
                s.pop_back();
            }
        }
        else if (op == "PeekMedian"){
            if (s.empty()) cout << "Invalid" << endl;
            else {
                vector<int> q(s);
                sort(q.begin(), q.end());
                cout << q[(q.size()+1)/2-1] << endl;
            }
        }
    }
    
    return 0;
}


// 3个测试点超时...