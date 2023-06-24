#include <iostream>
using namespace std;


class Node{
private:
    int data;
    Node *link;
    
public:
    Node(int i){data=i; link=nullptr;};
    void printData(){
        cout<<data<<"\n";
    }
    Node * getLink(){
        return link;
    }
    void setLink(Node *n){
        link=n;
    }
   
};

class LinkedQueue{
private:
    int size;
    Node *front;
    Node *back;
public:
    LinkedQueue(){size=0; front=back=nullptr;}
    ~LinkedQueue(){}
    bool isEmpty(){
        return front==nullptr;
    }
    int getSize(){
        return size;
    }
    void enqueue(Node *n){  //push
        if(n!=NULL){
            if(isEmpty()) front=back=n;
            else{
                back->setLink(n);
                back=n;
        }
            size++;
        }
    }
    Node* dequeue(){ //pop
        if(isEmpty()) return NULL;
        else{
            Node *tmp=front;
            front=front->getLink();
            size--;
            return tmp;
        }
}
    void printFront(){
        front->printData();
    }
    void printBack(){
        back->printData();
    }
    
};


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    int N;
    LinkedQueue Q;
    string str;
    cin>>N;
    for(int i=0;i<N;i++){
        cin>>str;
        if(str=="push"){
            int n;
            cin>>n;
            Q.enqueue(new Node(n));
        }
        else if (str=="pop"){
            Node *n=Q.dequeue();
            if(n==NULL) cout<<"-1\n";
            else n->printData();
        }
        else if (str=="size"){
            cout<<Q.getSize()<<"\n";
        }
        else if (str=="empty"){
            if(Q.isEmpty()) cout<<"1\n";
            else cout<<"0\n";
        }
        else if (str=="front"){
            if(Q.isEmpty()) cout<<"-1\n";
            else Q.printFront();
        }
        else if (str=="back"){
            if(Q.isEmpty()) cout<<"-1\n";
            else Q.printBack();
        }
    }
    
    return 0;
}



