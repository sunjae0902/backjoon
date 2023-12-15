#include <iostream>
using namespace std;
#define MAX 100000

class ArrStack{
private:
    int s_top=-1;
    int stack[MAX];
    
public:
    ArrStack(){}
    ~ArrStack(){}
    void push(int val){
        stack[++s_top]=val;
    }
    int pop(){
        if(empty()==1) return -1;
        int tmp=stack[s_top--];
        return tmp;
        
    }
    int top(){
        if(empty()==1) return -1;
        else return stack[s_top];
    }
    int size(){
        return s_top+1;
    }
    int empty(){
        if (s_top==-1) return 1;
        else return 0;
    }
    int getElement(int i) {return stack[i];}
    
};

int main() {
    int K;
    int total=0;
    ArrStack s;
    cin>>K;
    for(int i=0;i<K;i++) {
        int val;
        cin>>val;
        if(val==0) s.pop();
        else s.push(val);
        }
    for(int i=0;i<s.size();i++){
        total+=s.getElement(i);
    }
    cout<<total<<endl;
    
    return 0;
}
