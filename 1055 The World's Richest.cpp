#include<cstdio>
#include<iostream>
#include<string>
#include<algorithm>
using namespace std;

int n, k;

struct Stu{
    string name;
    int age;
    int w;
} s[100001];

bool cmp(Stu a, Stu b){
    if (a.w != b.w) return a.w > b.w;
    else if (a.age != b.age) return a.age < b.age;
    else return a.name < b.name;
}

void query(int m, int amin, int amax){
    int i, cnt=0;
    
    for (i=0; i<n && cnt<m; i++){
        if (s[i].age >= amin && s[i].age <= amax){
            printf("%s %d %d\n", s[i].name.c_str(), s[i].age, s[i].w);
            cnt++;
        }
    }
    
    if (cnt == 0){
        cout << "None" << endl;
    }
}

int main(){
    int i;
    cin>>n>>k;
    
    for (i=0; i<n; i++){
        cin >> s[i].name >> s[i].age >> s[i].w;
    }
    
    sort(s, s+n, cmp);
    
    for (i=1; i<k+1; i++){
        int x, amin, amax;
        
        cin >> x >> amin >> amax;
        
        printf("Case #%d:\n", i);
        query(x, amin, amax);
    }
    
    return 0;
}