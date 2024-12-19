//let titulo = document.querySelector('h1');
//titulo.innerHTML = 'Jogo do número secreto';

//let paragrafo = document.querySelector('p');
//paragrafo.innerHTML = 'Escolha um número entre 1 e 10';

function exibirTextoNaTela(tag, texto) {
    let campo = document.querySelector(tag)
    campo.innerHTML = texto
    
}

exibirTextoNaTela('h1', 'Jogo do número secreto')
exibirTextoNaTela('p', 'Escolha um número entre 1 e 10')

function verificarChute() {
    console.log('O botão foi clicado.')
}


//HTML Linguagem de marcação para estruturar conteúdo. Ex: <h1>Titulo</h1>
//CSS Linguagem de estilos para apresentação e estilização. Ex: p {color: red;} div{background-color: blue;}
//JavaScript(JS) Linguagem de porgramação para interatividade. Ex: function iniciarJogo(){...}