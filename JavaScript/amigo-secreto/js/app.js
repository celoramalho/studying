let nomes = []
function adicionar(){
    let novoNome = document.querySelector('#nome-amigo').value;
    if (novoNome == '') {
        alert('Nome inválido');
        return;
    }else if (nomes.includes(novoNome)){
        alert(`${novoNome} ja foi adicionado`);
        return;
    }else{
        nomes.push(novoNome);
        console.log(nomes);
        novoNome = '';
        atualizarListaAmigosAdicionados();
    }
}

function atualizarListaAmigosAdicionados(){
    let listaAmigos = document.querySelector('.friends__container')
    let separador = ',&nbsp';
    listaAmigos.innerHTML = '';

    for (let i = 0; i < nomes.length; i++) {
        if (i == nomes.length - 1) {
            separador = '';
        }
        console.log(nomes[i]);
        listaAmigos.innerHTML += `<p id="lista-amigos">${nomes[i]}${separador}</p>`;
    }
}


function sortear(){
    let listaSorteados = document.querySelector('.prizeDraw__container')
    listaSorteados.innerHTML = '';
    if (nomes.length % 2 != 0) {
        alert('Quantidade de nomes deve ser par');
        return;
    }else{
        let amigosSecretos = [];

        while (amigosSecretos.length < nomes.length) {
            amigo1 = nomes[parseInt(Math.random() * nomes.length)];
            amigo2 = nomes[parseInt(Math.random() * nomes.length)];

            if (amigosSecretos.includes(amigo1) || amigosSecretos.includes(amigo2) || amigo1 == amigo2) {
                continue;
            }else{
                amigosSecretos.push(amigo1, amigo2);
                console.log(`${amigo1} -> ${amigo2}`);
                listaSorteados.innerHTML  += `<p id="lista-sorteio">${amigo1} --> ${amigo2}</p>`
            }
        }
    }
}

function reiniciar(){
    nomes = [];
    atualizarListaAmigosAdicionados();
}