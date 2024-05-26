#include<bits/stdc++.h>
using namespace std;

int n, m , p;
int a, b , c, d , e, f;
int t[1005];
int s[1005][1005];
int g[1005][10005];

int result[12005];
int ketqua[10005];
vector<int> thesis[1005];
vector<int> teacher[1005];
int res = 0;
int curr = 0;

int caculate(){
    int result_1 = 0;
    for(int x=0; x<p; x++){
        int th = thesis[x].size();
        int t = teacher[x].size();
        for(int i=0; i<th;i++){
            for(int j=i+1; j<th; j++){
                result_1+=s[thesis[x][i]][thesis[x][j]];
            }
        }

        for(int i=0; i<th; i++){
            for(int j=0; j<t; j++){
                result_1+=g[thesis[x][i]][teacher[x][j]-n];
            }
        }
    }
    return result_1;
}

bool check(int k, int x){
    if (k<n){
        if(thesis[x].size()<b){
            return true;
        }
        else{
            return false;
        }
    }
    else{
        if(teacher[x].size()>d){
            return false;
        }
        else{
            for (int y : thesis[x]){
                if (t[y]==k-n+1){
                    return false;
                }
            }
            return true;
        }
    }
}

void Try(int k){
    for(int i=0; i<p; i++){
        if(check(k, i)){
            result[k]=i;
            if(k<n){
                thesis[i].push_back(k);
            }
            else{
                teacher[i].push_back(k);
            }

            if(k==n+m-1){
                bool check_1=true;
                for (int j=0; j<p; j++){
                    // cout<<thesis[j].size()<<" "<<teacher[j].size()<<endl;
                    if(thesis[j].size()<a && teacher[j].size()<c){
                        check_1=false;
                    }
                }
                // if(check_1){
                //     for(int j=0; j<m+n; j++){
                //         cout<<result[j]+1<<" ";
                //     }
                //     cout<<endl;
                // }
                bool check_2 = true;
                for(int x=0; x<p; x++){
                    int result_1 = 0;
                    int result_2 = 0;
                    int th = thesis[x].size();
                    int t = teacher[x].size();
                    for(int i=0; i<th;i++){
                        for(int j=0; j<th; j++){
                            result_1+=s[thesis[x][i]][thesis[x][j]];
                        }
                    }

                    for(int i=0; i<th; i++){
                        for(int j=0; j<t; j++){
                            result_2+=g[thesis[x][i]][teacher[x][j]-n];
                        }
                    }
                    if (result_1<e || result_2<f){
                        check_2=false;
                        break;
                    }
                }

                if (check_2 && check_1 && caculate()>res){
                    res=caculate();
                    for(int j=0; j<m+n; j++){
                        ketqua[j]=result[j];
                    }
                }
            }
            else{
                Try(k+1);
            }

            if(k<n){
                thesis[i].pop_back();
            }
            else{
                teacher[i].pop_back();
            }

        }
    }
}

int main(){
    cin >> n >> m >> p;
    cin >> a >> b >>c >> d >> e >>f;
    for (int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            cin >> s[i][j];
        }
    }

    for (int i = 0; i<n; i++){
        for(int j=0; j<m; j++){
            cin >> g[i][j];
        }
    }

    for (int i=0; i<n; i++){
        cin >> t[i];
    }

    Try(0);

    cout<<n<<endl;
    for(int i=0; i<n; i++){
        cout<<ketqua[i]+1<<" ";
    }
    cout<<endl;
    cout<<m<<endl;
    for(int i=n; i<m+n; i++){
        cout<<ketqua[i]+1<<" ";
    }
    cout<<endl;
    cout<<res;

}
