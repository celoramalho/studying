let amigos = [];

function adicionar() {
    const inputAmigo = document.querySelector('#nome-amigo');
    const novoAmigo = inputAmigo.value.trim();
    const novoAmigoLowerCase = novoAmigo.toLowerCase();

    if (!novoAmigo) {
        alert('Nome inválido');
        return;
    }

    if (amigos.some(amigo => amigo.toLowerCase() === novoAmigoLowerCase)) {
        alert(`${novoAmigo} já foi adicionado`);
        return;
    }

    amigos.push(novoAmigo);
    console.log(amigos);
    atualizarListaAmigos();
    limparInput(inputAmigo);
}

function atualizarListaAmigos() {
    const listaAmigos = document.querySelector('.friends__container');
    listaAmigos.innerHTML = amigos
        .map((amigo, index) => `<p id="lista-amigos">${amigo}${index < amigos.length - 1 ? ',&nbsp' : ''}</p>`)
        .join('');
}

function sortear() {
    const listaSorteados = document.querySelector('.prizeDraw__container');
    listaSorteados.innerHTML = '';

    if (amigos.length < 4) {
        alert('A quantidade de amigos deve ser maior que 3');
        return;
    }

    embaralharAmigos();

    const amigosSecretos = [];
    amigos.forEach((amigo, index) => {
        const proximoAmigo = amigos[(index + 1) % amigos.length];
        amigosSecretos.push([amigo, proximoAmigo]);
        listaSorteados.innerHTML += `<p id="lista-sorteio">${amigo} --> ${proximoAmigo}</p>`;
        console.log(`${amigo} -> ${proximoAmigo}`);
    });
}

function reiniciar() {
    amigos = [];
    atualizarListaAmigos();
    const listaSorteados = document.querySelector('.prizeDraw__container');
    listaSorteados.innerHTML = '';
}

function embaralharAmigos() {
    for (let i = amigos.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [amigos[i], amigos[j]] = [amigos[j], amigos[i]];
    }
    console.log('Amigos embaralhados:', amigos);
}

function limparInput(input) {
    input.value = '';
}