#include <iostream>

using namespace std;

int main(){
    cout << "*************************************" << endl;
    cout << "* Bem-Vindos ao jogo da adivinhação *" << endl;
    cout << "* ***********************************" << endl;

    const int NUMERO_SECRETO = 42; // IMUTAVEL
    // cout << "O número secreto é " << numero_secreto << endl;

    bool nao_acertou = true;
    int tentativas = 0;

    double pontos = 1000.0;

    while(nao_acertou){
        tentativas++;
        int chute;
        cout << "####Tentativa " << tentativas << "####" << endl;
        cout << "Qual seu chute: ";
        cin >> chute;

        double pontos_perdidos = abs(chute - NUMERO_SECRETO)/2.0;
        pontos = pontos - pontos_perdidos;

        bool acertou = (chute == NUMERO_SECRETO);
        bool maior = chute > NUMERO_SECRETO;
        
        if (acertou){
            cout << "Parabéns! Vocé acertou!" << endl;
            nao_acertou = false;
        }
        else if(maior){
            cout << "O seu chute foi maior que o número secreto" << endl;
        }
        else{
            cout << "O seu chute foi menor que o número secreto" << endl;
        }
    }
    cout << "Fim de jogo" << endl;
    cout << "Você acertou o número secreto em " << tentativas << " tentativas" << endl;
    cout.precision(2);
    cout << fixed;
    cout << "Sua pontuação foi de: " << pontos << " pontos." << endl;
}