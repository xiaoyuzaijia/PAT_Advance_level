#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;

struct Node{
    int add, key, next;
} a[100001];

int h, n, k;

int main(){
    scanf("%d %d %d", &h, &n, &k);
    int i;
    
    for (i=0; i<n; i++){
        int add;
        scanf("%d ", &add);
        a[add].add = add;
        scanf("%d %d\n", &a[add].key, &a[add].next);
    }
    
    vector<Node> rl;
    int p = h;
    int cnt = 0;
    while (p != -1){
        rl.push_back(a[p]);
        cnt++;
        if (cnt == k){
            reverse(rl.end()-k, rl.end());
            cnt = 0;
        }
        p = a[p].next;
    }
    
    for (i=0; i<(int)rl.size()-1; i++){
        printf("%05d %d %05d\n", rl[i].add, rl[i].key, rl[i+1].add);
    }
    printf("%05d %d -1\n", (rl.end()-1)->add, (rl.end()-1)->key);
    
    return 0;
}