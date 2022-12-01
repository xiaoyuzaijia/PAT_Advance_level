#include<iostream>
#include<cstring>
#include<vector>
#include<cmath>
#include<algorithm>
using namespace std;

int N, m, n, inde=0;
int a[10005];

bool can_vis(int x, int y, vector<vector<int>> mat){
    if (x<0 || x>=m || y<0 || y>=n) return false;
    else return (mat[x][y] == -1);
}

int main(){
    cin >> N;
    int i, j, x=0, y=0;
    
    for (i=0; i<N; i++){
        cin >> a[i];
    }
    sort(a, a+N);
    reverse(a, a+N);
    
    if (N == 1){
        cout << a[0] << endl;
        return 0;
    }
    
    for (i=ceil(sqrt(N)); i<=N; i++){
        if (N%i == 0){
            break;
        }
    }
    n = N / i;
    m = i;
    
    int mat[m][n];
    memset(mat, -1, sizeof(int)*m*n);
    int forward=0;
    int X[] = {0, 1, 0, -1};
    int Y[] = {1, 0, -1, 0};
    
    while (true){
        if (inde == N) break;
        mat[x][y] = a[inde++];
        if (x+X[forward]<0 || x+X[forward]>=m || y+Y[forward]<0 || y+Y[forward]>=n || mat[x+X[forward]][y+Y[forward]] != -1){
            forward = (forward+1)%4;
        }
        x += X[forward];
        y += Y[forward];
        
    }
    
    for (i=0; i<m; i++){
        for (j=0; j<n-1; j++){
            cout << mat[i][j] << ' ';
        }
        cout << mat[i][j] << endl;
    }
    
    return 0;
}