#include <iostream>
//using namespace std;

//Com uma constante definindo o tamanho do vetor, da mais clareza e o torna mais escalonável
const int NUM_ELEM = 10;

int main(){
    int c[NUM_ELEM];
    for (int i = 0; i < NUM_ELEM; i++)
    {
        c[i] = 2 * i;
    }
    
    for (int i = 0; i < NUM_ELEM; i++)
    {
        std::cout << "c[" << i << "] = " << c[i] << "\n";
    }
    return 0;
}