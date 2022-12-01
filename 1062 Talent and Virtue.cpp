#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;

int n, l, h, m = 0;

struct Stu{
    int id;
    int v;
    int t;
    int all;
} s[100005];

bool cmp(Stu a, Stu b){
    if (a.all != b.all) return a.all > b.all;
    else if (a.v != b.v) return a.v > b.v;
    else return a.id < b.id;
}

int main(){
    int i;
    vector<Stu> sage, noble, fool, small;
    scanf("%d %d %d", &n, &l, &h);
    
    int id, v, t;
    for (i=0; i<n; i++){
        scanf("%d %d %d", &id, &v, &t);
        if (v >= l && t >= l){
            m++;
            Stu p;
            p.id = id;
            p.v = v;
            p.t = t;
            p.all = v + t;
            if (v >= h && t >= h) sage.push_back(p);
            else if (v >= h && t < h) noble.push_back(p);
            else if (v < h && t < h && v >= t) fool.push_back(p);
            else small.push_back(p);
        }
    }
    
    sort(sage.begin(), sage.end(), cmp);
    sort(noble.begin(), noble.end(), cmp);
    sort(fool.begin(), fool.end(), cmp);
    sort(small.begin(), small.end(), cmp);
    
    sage.insert(sage.end(), noble.begin(), noble.end());
    sage.insert(sage.end(), fool.begin(), fool.end());
    sage.insert(sage.end(), small.begin(), small.end());
    
    printf("%d\n", m);
    for (i=0; i<m; i++){
        if (i == m-1) printf("%08d %d %d", sage[i].id, sage[i].v, sage[i].t);
        else printf("%08d %d %d\n", sage[i].id, sage[i].v, sage[i].t);
    }
    return 0;
}