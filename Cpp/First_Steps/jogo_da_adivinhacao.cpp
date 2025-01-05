#include <iostream>

using namespace std;

int main(){
    cout << "*************************************" << endl;
    cout << "* Bem-Vindos ao jogo da adivinhação *" << endl;
    cout << "* ***********************************" << endl;

    const int NUMERO_SECRETO = 42; // IMUTAVEL
    // cout << "O número secreto é " << numero_secreto << endl;

    int chute;
    cout << "Qual seu chute: ";
    cin >> chute;
    cout << "O seu chute foi " << chute << endl;


    bool acertou = (chute == NUMERO_SECRETO);
    bool maior = chute > NUMERO_SECRETO;
    
    if (acertou){
        cout << "Parabéns! Vocé acertou!" << endl;
    }
    else if(maior){
        cout << "O seu chute foi maior que o número secreto" << endl;
    }
    else{
        cout << "O seu chute foi menor que o número secreto" << endl;
    }
}