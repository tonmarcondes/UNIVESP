#include <cstddef>
#include <iostream>

using namespace std;

void funcao1(int*& p){
    p = new int;
    *p = 8;
}
void funcao2(int* p){
    p = new int;
    *p = 8;
}
int main(){
    int* a = new int;
    int* b = new int;

    *a = 2;
    *b = 3;
    
    funcao1(a);
    funcao2(b);

    cout << *a << endl;
    cout << *b << endl;
} 
// RESP: 8 e 3