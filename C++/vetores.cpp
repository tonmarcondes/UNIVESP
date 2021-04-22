#include <iostream>

using namespace std;

int main(){
    //inicializando o vetor de 10 elementos e declarando apenas 3 os demais são preenchidos por 0
    int c[10] = {14, 0, 13};

    for (int i = 0; i < 10; i++)
    {
        //c[i] += i;
        cout << "c[" << i << "] = " << c[i] << "\n";
    }
    
}