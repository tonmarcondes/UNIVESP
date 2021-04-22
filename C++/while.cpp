#include <iostream>

int number;
int counter = 0;
int amount = 0;

int main(){
  while (counter < 10){
      std::cout << "digite um número qualquer (" << counter << ")\n";
      std::cin >> number;

      if (number < 5){
          amount++;
      }

    counter++;
  }
