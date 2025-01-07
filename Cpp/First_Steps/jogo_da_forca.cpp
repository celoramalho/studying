#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <fstream>
#include <ctime>
#include <cstdlib>

using namespace std;

const int LIMITE_CHUTES = 8;

string palavra_secreta;
map<char, bool> chutou;
vector<char> chutes_errados;

void imprime_cabecalho() {
    cout << "*************************************" << endl;
    cout << "*           Jogo da Forca!          *" << endl;
    cout << "*************************************" << endl;
    cout << endl;
}

string converte_string_para_maiuscula(string palavra) {
    string palavra_maiuscula;
    for (size_t i = 0; i < palavra.size(); i++) {
        palavra_maiuscula += toupper(palavra[i]);
    }
    return palavra_maiuscula;
}

void imprime_erros() {
    cout << "Chutes errados: ";
    for (size_t i = 0; i < chutes_errados.size(); i++) {
        cout << chutes_errados[i] << ", ";
    }
    cout << endl;
}

void imprime_palavra() {
    for (size_t i = 0; i < palavra_secreta.size(); i++) {
        char letra = palavra_secreta[i];
        if (chutou[letra]) {
            cout << letra << " ";
        } else {
            cout << "_ ";
        }
    }
    cout << endl;
}

bool letra_existe(char chute) {
    for (size_t i = 0; i < palavra_secreta.size(); i++) {
        if (palavra_secreta[i] == chute) {
            return true;
        }
    }
    return false;
}

bool nao_acertou() {
    for (size_t i = 0; i < palavra_secreta.size(); i++) {
        if (!chutou[palavra_secreta[i]]) {
            return true;
        }
    }
    return false;
}

void chuta() {
    char chute;
    cout << "Digite uma letra: ";
    cin >> chute;
    chute = toupper(chute);

    chutou[chute] = true;

    if (letra_existe(chute)) {
        cout << "Você acertou! A letra está na palavra" << endl;
    } else {
        cout << "Ops, você errou! A letra não está na palavra" << endl;
        chutes_errados.push_back(chute);
    }
    cout << endl;
}

vector<string> le_arquivo() {
    ifstream arquivo;
    arquivo.open("palavras.txt");

    if (arquivo.is_open()) {
        int quantidade_palavras;
        arquivo >> quantidade_palavras;

        vector<string> palavras_do_arquivo;

        if (quantidade_palavras == 0) {
            cout << "Arquivo vazio" << endl;
            exit(0);
        }

        for (int i = 0; i < quantidade_palavras; i++) {
            string palavra_lida;
            arquivo >> palavra_lida;
            palavra_lida = converte_string_para_maiuscula(palavra_lida);
            palavras_do_arquivo.push_back(palavra_lida);
        }

        arquivo.close();
        return palavras_do_arquivo;
    } else {
        cout << "Não foi possível abrir o arquivo" << endl;
        exit(0);
    }
}

void sorteia_palavra() {
    vector<string> palavras = le_arquivo();
    srand((unsigned int)time(NULL));
    int indice_sorteado = rand() % palavras.size();
    palavra_secreta = palavras[indice_sorteado];
}

void salva_arquivo(vector<string> nova_lista) {
    ofstream arquivo;
    arquivo.open("palavras.txt");

    if (arquivo.is_open()) {
        arquivo << nova_lista.size() << endl;

        for (size_t i = 0; i < nova_lista.size(); i++) {
            arquivo << nova_lista[i] << endl;
        }

        arquivo.close();
    } else {
        cout << "Arquivo não pode ser aberto" << endl;
    }
}

void adicionar_palavra() {
    cout << "Digite a palavra: ";
    string nova_palavra;
    cin >> nova_palavra;

    vector<string> lista_palavras = le_arquivo();
    lista_palavras.push_back(nova_palavra);

    salva_arquivo(lista_palavras);
}

int main() {
    imprime_cabecalho();

    sorteia_palavra();

    while (nao_acertou() && chutes_errados.size() < LIMITE_CHUTES) {
        imprime_erros();
        imprime_palavra();
        chuta();
    }

    cout << "Fim de jogo!\nA palavra era " << palavra_secreta << endl;
    if (nao_acertou()) {
        cout << "Que pena, você perdeu!" << endl;
    } else {
        cout << "Parabéns, você ganhou!\n";

        cout << "Você deseja adicionar uma nova palavra ao banco de palavras? (S/N)" << endl;
        char resposta;
        cin >> resposta;
        if (toupper(resposta) == 'S') {
            adicionar_palavra();
            cout << "Palavra adicionada com sucesso!" << endl;
        }
    }
    return 0;
}