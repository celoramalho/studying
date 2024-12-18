alert('Boas vindas ao jogo do número secreto');
let numeroSecreto = 29;//In JavaScript we use camelCase
console.log('O numero secreto é ' + numeroSecreto)
let chute = prompt('Escolha um número entre 1 e 30')

if (chute == numeroSecreto) {
    alert('Parabens, vocé acertou'); //Mensagem exibida no console
} else {
    alert('Que pena, vocé errou :(')
}
//camelCase
//snake_case
//PascalCase