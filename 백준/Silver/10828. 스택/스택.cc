#include <iostream>
using namespace std;
#define MAX 10000

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
    
};

int main(int argc, const char * argv[]) {
    int N;
    ArrStack s;
    cin>>N;
    for(int i=0;i<N;i++) {
        int val;
        string m;
        cin>>m;
        if(m=="push"){
            cin>>val;
            s.push(val);
        }
        else{
            if(m=="pop"){
                cout<<s.pop()<<endl;
        }
            else if(m=="size"){
                cout<<s.size()<<endl;
        }
            else if(m=="empty"){
                cout<<s.empty()<<endl;
        }
            else if(m=="top"){
                cout<<s.top()<<endl;
        }
        }
    }
    
    return 0;
}
