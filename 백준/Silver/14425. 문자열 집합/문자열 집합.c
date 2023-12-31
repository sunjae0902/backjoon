#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUCKET 100

typedef struct Node{
    char data[500];
    struct Node *next;
}Node;

typedef struct{
    int count;
    Node *head;
}Bucket;

void init_htable(Bucket *htable){ // 해시 테이블 초기화
    for(int i=0;i<BUCKET;i++){
        htable[i].head = NULL;
        htable[i].count = 0;
    }
}

int hashFunc(char key[]){ // 해시 함수
    int sum=0;
    int power=1;
    for(int i=0;key[i]!='\0';i++){
        sum+=key[i];
       // power*=2;
    }
    return sum%BUCKET;
    
}
void add_value(Bucket *htable, char input[]){
    int hashIndex = hashFunc(input);

    Node *n = (Node *)malloc(sizeof(Node)); // 메모리 할당
   
    strcpy(n->data,input);
    n->next = NULL; // 값 저장
    
    if(htable[hashIndex].head == NULL) // 아직 노드가 없을 경우
        htable[hashIndex].head = n;
    
    else {
        Node *current = htable[hashIndex].head;
        while(current->next != NULL){ // 연결 리스트 최하단에 삽입
            current = current->next;
        }
        current->next = n;
    }
    htable[hashIndex].count++; // 1 증가시켜줌
    return;
    
}
int search(Bucket *htable, char input[]){
    int hashIndex = hashFunc(input);
    int i;
    Node *h = htable[hashIndex].head;
    while(h != NULL){
        if(strcmp(h->data,input) == 0) return 1;
        h = h->next;
    }
    return -1;
    
}



int main(void){
    int N,M,cnt=0;
    
    Bucket htable[BUCKET];
    init_htable(htable); //초기화
    
    scanf("%d %d",&N,&M);
    
    for (int i = 0; i < N; i++) {
        char temp[500];
        scanf("%s", temp);
        if(search(htable,temp)!=1)
            add_value(htable, temp);
    }
    
    for (int i = 0; i < M; i++) {
        char temp[500];
        scanf("%s", temp);
        if(search(htable,temp)==1) cnt++;
    }


    printf("%d\n",cnt);
    
    for (int i = 0; i < BUCKET; i++) {
        Node *current = htable[i].head;
        while (current != NULL) {
            Node *next = current->next;
            free(current);
               current = next;
           }
       }
    
    
    return 0;
}
