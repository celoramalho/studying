#include <iostream>

using namespace std;

int main(){
    cout << "*************************************" << endl;
    cout << "* Bem-Vindos ao jogo da adivinhação *" << endl;
    cout << "* ***********************************" << endl;

    int numero_secreto = 42;
    // 42cout << "O número secreto é " << numero_secreto << endl;

    int chute;
    cout << "Qual seu chute: ";
    cin >> chute;
    cout << "O seu chute foi " << chute << endl;

    if (chute == numero_secreto){
        cout << "Parabéns! Vocé acertou!" << endl;
    }
    else if(chute > numero_secreto){
        cout << "O seu chute foi maior que o número secreto" << endl;
    }
    else{
        cout << "O seu chute foi menor que o número secreto" << endl;
    }

}