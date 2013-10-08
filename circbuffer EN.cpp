#include <iostream>
#include <string>

using namespace std;

/**   
   LinkedList - time complexity
   get (by pointer) O(1) (Actually takes max 7 instructions which is still constant)
   set (by pointer) O(1) (Actually takes max 7 instructions which is still constant)
   removeLast O(1) (Actually takes max 5 instructions which is still constant)
   add O(1) (Actually takes max 10 instructions which is still constant)
   removeLastN O(n)
   removeAll O(n)
**/
typedef struct Element{
   string value;
   Element *next;
   Element *prev;
} Element;

Element *head = (Element *)NULL, *tail = (Element *)NULL;
int bufferSize = 0, maxSize = 0;

void removeFirst(){
   if(head == NULL){
      return;
   }
   else if(head == tail){
      head = NULL;
      delete tail;
      tail = NULL;
   }
   else{
      head = head->next;
      head->prev->next = NULL;
      delete head->prev;
      head->prev = NULL;
   }
   bufferSize--;
}

void append(string v){
   Element *e = new Element;
   e->value = v;
   if(head == NULL){
      head = e;
      tail = head;
      e->next = NULL;
      e->prev = NULL;
   }
   else{
      e->next = NULL;
      tail->next = e;
      e->prev = tail;
      tail = e;
   }
   bufferSize++;
   e= NULL;
   if(bufferSize > maxSize){
      removeFirst();
   }
   
}

void removeFirstN(int n){
   while(n >0){
      if(head == NULL){
         return;
      }
      else if(head == tail){
         head = NULL;
         delete tail;
         tail = NULL;
		 bufferSize--;
         return;
      }
      else{
         head = head->next;
         head->prev->next = NULL;
         delete head->prev;
         head->prev = NULL;
      }
      bufferSize--;
      n--;
   } 
}

void bufferList(){
   Element * p = head;
   while(p != NULL){
      cout<<p->value<<"\n";
      p=p->next;
   }
}

int mainRun2() {
   std::ios_base::sync_with_stdio(false);
   int app;
   char command;
   string value;
   cin>>maxSize>>command;   
   while(command != 'Q' ){
       switch(command){
            case 'A':
               cin>>app;
               for(int i=0; i<app; i++){
                  cin>>value;
                  append(value);
               }
            break;
            case 'R':
               cin>>app;
               removeFirstN(app);
            break;
            case 'L':
               bufferList();
            break;
			case 'S':
				cout<<bufferSize<<endl;
            default:
            break;
       }
       cin>>command;       
   }
   return 0;
}