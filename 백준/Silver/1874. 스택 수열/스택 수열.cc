#include "iostream"
#include <stack>
#include <vector>
using namespace std;


int main(){
    int n;
    cin>>n;
    int arr[n];
    stack<int> s;
    vector<char> res;
    for(int i=0;i<n;i++) cin>>arr[i];
    int j=1,i=0;
    while(i<n || j<=n){
        if(!s.empty() && s.top()==arr[i]) {
            s.pop();
            res.push_back('-');
            i++;
        }
        else{
            if(j>arr[i]) break;
            while (j<=arr[i]){
                s.push(j++);
                res.push_back('+');
            }
        }
            
        }
    if(!s.empty())  cout<<"NO\n";
    else for(char c:res) cout<<c<<'\n';
    return 0;
        
}
  
    

