#include<iostream>
#include<string>
using namespace std;

int mod=1000000007;
string s;
int T[100001], AT[100001], PAT[100001];

int main(){
    cin >> s;
    int i, n=s.size();
    
    if (s[n-1] == 'T') T[n-1] = 1;
    for (i=n-2; i>=0; i--){
        if (s[i] == 'T'){
            T[i] = (T[i+1] + 1) % mod;
            AT[i] = AT[i+1];
            PAT[i] = PAT[i+1];
        }
        else if (s[i] == 'A'){
            T[i] = T[i+1];
            AT[i] = (AT[i+1] + T[i+1]) % mod;
            PAT[i] = PAT[i+1];
        }
        else if (s[i] == 'P'){
            T[i] = T[i+1];
            AT[i] = AT[i+1];
            PAT[i] = (PAT[i+1] + AT[i+1]) % mod;
        }
    }
    
    cout << PAT[0] << endl;
    
    return 0;
}