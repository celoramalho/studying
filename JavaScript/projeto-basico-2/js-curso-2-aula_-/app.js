let numeroSecreto = gerarNumeroAleatorio();
let tentativas = 1;
//let titulo = document.querySelector('h1');
//titulo.innerHTML = 'Jogo do número secreto';

//let paragrafo = document.querySelector('p');
//paragrafo.innerHTML = 'Escolha um número entre 1 e 10';

function exibirTextoNaTela(tag, texto) {
    let campo = document.querySelector(tag);
    campo.innerHTML = texto;
}

exibirTextoNaTela('h1', 'Jogo do número secreto');
exibirTextoNaTela('p', 'Escolha um número entre 1 e 10');

function verificarChute() {
    let chute = document.querySelector('input').value;
    console.log(`Número chutado: ${chute}`);
    console.log(`Número Secreto: ${numeroSecreto}`);
    console.log(chute == numeroSecreto);
    if (chute == numeroSecreto) {
        let palavraTentativa = tentativas > 1 ? 'tentativas' : 'tentativa';
        let mensagemTentativa = `Você descobriu o número secreto com ${tentativas} ${palavraTentativa}!`
        exibirTextoNaTela('h1', 'Parabéns!');
        exibirTextoNaTela('p', mensagemTentativa);
    } else {
        exibirTextoNaTela('h1', 'Que pena, vocé errou!');
        if (chute > numeroSecreto){
            exibirTextoNaTela('p', 'O número secreto é menor');
        } else {
            exibirTextoNaTela('p', 'O número secreto é maior');
        }
        tentativas++;
        limparCampo();
    }
}

function gerarNumeroAleatorio() {
    return parseInt(Math.random() * 10 + 1);
}

function limparCampo() {
    let chute = document.querySelector('input');
    chute.value = '';
}

//HTML Linguagem de marcação para estruturar conteúdo. Ex: <h1>Titulo</h1>
//CSS Linguagem de estilos para apresentação e estilização. Ex: p {color: red;} div{background-color: blue;}
//JavaScript(JS) Linguagem de porgramação para interatividade. Ex: function iniciarJogo(){...}