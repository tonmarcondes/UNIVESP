#include <iostream>

using namespace std;

int total = 0;
int num = 15;
float avg = 0;

int main(){

    do
    {
        cout << "Insira um valor para o teste: " << endl;
        //cin >> num;
        total+= num;
        avg++;
    } while (num != 0);

    cout << "\nForam inseridos " << avg << " mnúmeros" << endl;
    cout << "com uma soma total de " << total << endl;
    cout << "\nE sua média foi de  " << total / (avg -1) << "\n\n";
    
}