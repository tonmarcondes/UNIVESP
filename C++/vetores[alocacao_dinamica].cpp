#include <iostream>
//using namespace std;

int main(){
    int num_elemen;
    std::cout << "Informe o tamanho do vetor: ";
    std::cin >> num_elemen;

    int *c = new int[num_elemen];

    for (int i = 0; i < num_elemen; i++)
    {
        c[i] = 2 * i;
        std::cout << "c[" << i << "] = " << c[i] << "\n";
    }
    //A Alocação de um vetor dinêmico
    int *d = new int [num_elemen];

    //A desalocação de um vetor dinêmico é feito
    delete [] d;
}