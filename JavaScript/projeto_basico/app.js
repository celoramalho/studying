alert('Boas vindas ao jogo do número secreto');
let numeroSecreto = 13;//In JavaScript we use camelCase
console.log('O numero secreto é ' + numeroSecreto)
let chute = prompt('Escolha um número entre 1 e 30')

if (chute == numeroSecreto) {
    alert(`Parabens, vocé acertou o número secreto ${chute}`); //Mensagem exibida no console; Template string pra concatenação
} else {
    if (chute > numeroSecreto) {
        alert(`O número secreto é menor que ${chute}`)
    } else {
        alert(`O número secreto é maior que ${chute}`)
    }
}
//camelCase
//snake_case
//PascalCase