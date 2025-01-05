#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main(){
    cout << "*************************************" << endl;
    cout << "* Bem-Vindos ao jogo da adivinhação *" << endl;
    cout << "* ***********************************" << endl;

    cout << "Escolha seu nível de dificuldade: " << endl;
    cout << "(F) - Facil" << endl;
    cout << "(M) - Medio" << endl;
    cout << "(D) - Dificil" << endl;

    char dificuldade;
    cin >> dificuldade;
    int numero_de_tentativas;

    if (dificuldade == 'F'){
        numero_de_tentativas = 15;
    }
    else if(dificuldade == 'M'){
        numero_de_tentativas = 10;
    }
    else{
        numero_de_tentativas = 5;
    }

    srand(time(NULL));
    const int NUMERO_SECRETO = rand() % 100; // IMUTAVEL
    // cout << "O número secreto é " << NUMERO_SECRETO << endl;

    bool nao_acertou = true;
    int tentativas = 1;

    double pontos = 1000.0;

    for(tentativas; tentativas <= numero_de_tentativas; tentativas++){
        int chute;
        cout << "\n#### Tentativa " << tentativas << " ####" << endl;
        cout << "Qual seu chute: ";
        cin >> chute;

        double pontos_perdidos = abs(chute - NUMERO_SECRETO)/2.0;
        pontos -= pontos_perdidos;

        bool acertou = (chute == NUMERO_SECRETO);
        bool maior = chute > NUMERO_SECRETO;
        
        if (acertou){
            cout << "Parabéns! Vocé acertou!" << endl;
            nao_acertou = false;
            break;
        }
        else if(maior){
            cout << "O seu chute foi maior que o número secreto" << endl;
        }
        else{
            cout << "O seu chute foi menor que o número secreto" << endl;
        }
    }

    cout << "Fim de jogo" << endl;
    if (nao_acertou){
        cout << "Puxa, vocé errou o número secreto era " << NUMERO_SECRETO << endl;
    }else{
        cout << "Você acertou o número secreto em " << tentativas << " tentativas" << endl;
        cout.precision(2);
        cout << fixed;
        cout << "Sua pontuação foi de: " << pontos << " pontos." << endl;
    }
}