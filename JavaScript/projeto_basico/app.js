alert('Boas vindas ao jogo do número secreto');
let numeroMaximo = 100
let numeroSecreto = parseInt(Math.random() * numeroMaximo + 1); //pseudo-aleatorio
console.log('O numero secreto é ' + numeroSecreto); // Linter puts automatically ;
let chute
let tentativas = 1;
//In JavaScript we use camelCase
//enquanto o chute for diferente do numero secreto
while (chute != numeroSecreto) {
    chute = prompt(`Escolha um número entre 1 e ${numeroMaximo}`);
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
// https://www.w3schools.com/js/default.asp
//Operadores de comparação > < >= <= == !=