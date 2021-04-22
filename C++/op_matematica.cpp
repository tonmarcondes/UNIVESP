#include <iostream>

float number1;
float number2;

int main(){
  std::cout << "\nDigite o 1° número para a soma: ";
  std::cin >> number1;
  std::cout << "Digite o 2° número para a soma: ";
  std::cin >> number2;

  std::cout << "\nA soma dos dois númenros é " << number1 + number2 << "\n";
  std::cout << "A subtração dos dois númenros é " << number1 - number2 << "\n";
  std::cout << "A multiplicação dos dois númenros é " << number1 * number2 << "\n";
  std::cout << "A divisão dos dois númenros é " << number1 / number2 << "\n\n";

}