#include<bits/stdc++.h>
using namespace std;

struct Record{
    string id;
    int t;
    string st;
    Record(string __id, int __t, string __st){
        id = __id;
        t = __t;
        st = __st;
    }
};

int n, k, max_p_time=0;
vector<Record> rr;
vector<Record> r;
map<string, int> p_time;

int t_from_zore(int h, int m, int s){
    return h*3600 + m*60 + s;
}

bool cmp(Record a, Record b){
    return a.t < b.t;
}

int main(){
    cin >> n >> k;
    int i, j;
    
    for (i=0; i<n; i++){
        string id, st;
        int h, m, s;
        cin >> id;
        scanf("%d:%d:%d", &h, &m, &s);
        cin >> st;
        rr.push_back(Record(id, t_from_zore(h, m, s), st));
        p_time[id] = 0;
    }
    
    sort(rr.begin(), rr.end(), cmp);
    
    for (i=0; i<n; i++){
        if (rr[i].st == "in"){
            for (j=i+1; j<n; j++){
                if (rr[j].id == rr[i].id and rr[j].st == "out"){
                    r.push_back(rr[i]);
                    r.push_back(rr[j]);
                    p_time[rr[i].id] += rr[j].t - rr[i].t;
                    if (max_p_time < p_time[rr[i].id]) max_p_time = p_time[rr[i].id];
                    break;
                }
                else if (rr[j].id == rr[i].id and rr[j].st == "in"){
                    break;
                }
            }
        }
    }
    
    sort(r.begin(), r.end(), cmp);
    
    
    int h, m, s, qt;
    int t=0, curr_p=0;
    
    
    scanf("%d:%d:%d", &h, &m, &s);
    qt = t_from_zore(h, m, s);
    
    
    j = 0;
    while (t <= 24*3600){
        while (t == r[j].t){
//          cout << r[j].id << ' '<< r[j].t << ' ' << r[j].st <<endl;
            if (r[j].st == "in") curr_p++;
            else curr_p--;
            j++;
        }
        
        if (k > 0 and t == qt){
            cout << curr_p << endl;
            scanf("%d:%d:%d", &h, &m, &s);
            qt = t_from_zore(h, m, s);
            k--;
        }
        
        t++;
    }
    
    for (map<string, int>::iterator it = p_time.begin(); it != p_time.end(); it++){
        if (it->second == max_p_time){
            cout << it->first << ' ';
        }
    }
    printf("%02d:%02d:%02d\n", max_p_time/3600, max_p_time%3600/60, max_p_time%60);
    
    return 0;
}
