#include <iostream>
#include <cstring>
using namespace std;
#define MAX 100000

class ArrStack{
private:
    int s_top=-1;
    char stack[MAX];
    
public:
    ArrStack(){}
    ~ArrStack(){}
    void push(char val){
        stack[++s_top]=val;
    }
    char pop(){
        if(empty()==1) return -1;
        int tmp=stack[s_top--];
        return tmp;
        
    }
    char top(){
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
    char getElement(int i) {return stack[i];}
    
};

int isVPS(ArrStack &s,string str){
    for(int i=0;i<str.length();i++){
        if(str.at(i)=='(') s.push(str.at(i));
        else{ //닫는 괄호 만남
            if(s.empty()==1) { //비어있는 경우
                return -1;
            }
            else{
                char a=s.top(); //비어있지 않은 경우
                if(a!=str.at(i)) s.pop(); //비어있지 않고 짝 일치
                else { //비어있지 않은데 짝이 안맞는 경우
                    return -1;
            }
            }
   }
}
    if(s.empty()==1) return 1;
    else return -1;
    
}

int main() {
    int T;
    cin>>T;
    for(int i=0;i<T;i++) {
        ArrStack s;
        string str;
        cin>>str;
        int res=isVPS(s,str);
        if(res==-1) cout<<"NO\n";
        else cout<<"YES\n";
    }
    return 0;
}
