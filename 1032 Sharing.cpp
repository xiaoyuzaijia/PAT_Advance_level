#include<cstdio>
using namespace std;

struct Chr{
    char c;
    int next;
    int flag = 0;
} a[100001];

int n, ah, bh;

int main(){
    scanf("%d %d %d", &ah, &bh, &n);
    int i;
    
    
    for (i=0; i<n; i++){
        int id;
        scanf("%d ", &id);
        scanf("%c %d", &a[id].c, &a[id].next);
    }
    
    int p = ah;
    while (p != -1){
        a[p].flag = 1;
        p = a[p].next;
    }
    
    p = bh;
    while (p != -1){
        if (a[p].flag == 1){
            printf("%05d\n", p);
            return 0;
        }
        p = a[p].next;
    }
    
    printf("-1\n");
    
    return 0;
}
