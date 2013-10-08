#include <iostream>
#include <unordered_map>
#include <forward_list>
#include <string>
#include <functional>
using namespace std;
typedef struct node{
	string t;
	int i;
	bool operator>(const node s) const {
		if (i == s.i)
			return t<s.t;
		else
			return i > s.i;
    }
} node;
std::unordered_map<string, node *> terms;
std::forward_list<node> termStack;
void add(string term){
	if(terms.find(term) == terms.end()){
		node *n = new node;
		n->t=term;
		n->i=1;
		termStack.push_front(*n);
		terms[term]=&termStack.front();			
	}
	else{
		terms[term]->i++;
	}
}
void get(int k){
	termStack.sort(std::greater<node>());
	for(int i=0; i<k; i++){
		cout<<termStack.front().t<<endl;
		termStack.pop_front();
	}
}
int mainRun(){
	std::ios_base::sync_with_stdio(false);
	int numT;
	string t;
	cin>>numT;
	for(int i=0; i<numT; i++){
		cin>>t;
		add(t);
	}
	cin>>numT;
	get(numT);
	return 0;
}