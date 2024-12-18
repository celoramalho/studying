alert('Boas vindas ao jogo do número secreto');
let numeroSecreto = 13;//In JavaScript we use camelCase
console.log('O numero secreto é ' + numeroSecreto); // Linter puts automatically ;
let chute
let tentativas = 1;

//enquanto o chute for diferente do numero secreto
while (chute != numeroSecreto) {
    chute = prompt('Escolha um número entre 1 e 30');
    if (chute == numeroSecreto) {
        break;
        
    } else {
        if (chute > numeroSecreto) {
            alert(`O número secreto é menor que ${chute}`);
        } else {
            alert(`O número secreto é maior que ${chute}`);
        }
        tentativas++; //tentativas = tentativas + 1; ++ para incrementar um
    }
}
let palavraTentativa = tentativas > 1 ? 'tentativas' : 'tentativa' //Operador ternario
alert(`Parabens, vocé acertou o número secreto ${chute} com ${tentativas} ${palavraTentativa}`); //Mensagem exibida no console; Template string pra concatenação
//camelCase
//snake_case
//PascalCase

//Operadores de comparação > < >= <= == !=