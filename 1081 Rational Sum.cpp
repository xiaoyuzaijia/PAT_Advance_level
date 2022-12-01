#include<iostream>
#include<cstdio>
using namespace std;

typedef long long int LL;
int n;
LL sa, sb;

LL gcd(LL a, LL b){
    if (a<b) swap(a, b);
    if (b == 0) return a;
    else return gcd(b, a%b);
}

void add(LL a, LL b){
    LL c;
    
    sa = a * sb + b * sa;
    sb = b * sb;
    
    c = gcd(abs(sa), abs(sb));
    sa /= c;
    sb /= c;
}

int main(){
    int i;
    cin >> n;
    
    scanf("%lld/%lld ", &sa, &sb);
    for (i=1; i<n; i++){
        LL a, b;
        scanf("%lld/%lld ", &a, &b);
        add(a, b);
    }
    
    if (sa < 0){
        cout << '-';
        sa = -sa;
    }
    if (sa == 0){
        cout << '0';
        return 0;
    }
    if (sa >= sb){
        printf("%lld", sa/sb);
        sa = sa%sb;
        if (sa != 0){
            printf(" %lld/%lld", sa, sb);
        }
    }
    else{
        printf("%lld/%lld", sa, sb);
    }
    
    cout << endl;
    
    return 0;
}
