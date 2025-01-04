let amigos = []
function adicionar(){
    let novoAmigo= document.querySelector('#nome-amigo').value;
    if (novoAmigo == '') {
        alert('Nome inválido');
        return;
    }else if (amigos.includes(novoAmigo)){
        alert(`${novoAmigo} ja foi adicionado`);
        return;
    }else{
        amigos.push(novoAmigo);
        console.log(amigos);
        novoAmigo = '';
        atualizarListaAmigosAdicionados();
    }
}

function atualizarListaAmigosAdicionados(){
    let listaAmigos = document.querySelector('.friends__container')
    let separador = ',&nbsp';
    listaAmigos.innerHTML = '';

    for (let i = 0; i < amigos.length; i++) {
        if (i == amigos.length - 1) {
            separador = '';
        }
        console.log(amigos[i]);
        listaAmigos.innerHTML += `<p id="lista-amigos">${amigos[i]}${separador}</p>`;
    }
}


function sortear(){
    let listaSorteados = document.querySelector('.prizeDraw__container')
    listaSorteados.innerHTML = '';
    if (amigos.length % 2 != 0) {
        alert('Quantidade de amigos deve ser par');
        return;
    }else{
        let amigosSecretos = [];
        
        for (let i = amigos.length; i > 0; i--) {
            
            const indexRandom = parseInt(Math.random() * i);

            [amigos[i - 1], amigos[indexRandom]] = [amigos[indexRandom], amigos[i-1]];
            
        }
        console.log(amigos);

        for (let i = 0; i < amigos.length; i++) {
            if (i == amigos.length - 1) {
                amigosSecretos.push(amigos[i], amigos[0]);
                console.log(`${amigos[i]} -> ${amigos[0]}`);
                listaSorteados.innerHTML  += `<p id="lista-sorteio">${amigos[i]} --> ${amigos[0]}</p>`
            }else{
                amigosSecretos.push(amigos[i], amigos[i + 1]);
                console.log(`${amigos[i]} -> ${amigos[i + 1]}`);
                listaSorteados.innerHTML  += `<p id="lista-sorteio">${amigos[i]} --> ${amigos[i + 1]}</p>`
            }   
        }
    }
}

function reiniciar(){
    amigos = [];
    atualizarListaAmigosAdicionados();
}



//        while (amigosSecretos.length < amigos.length) {
//            amigo1 = amigos[parseInt(Math.random() * amigos.length)];
//            amigo2 = amigos[parseInt(Math.random() * amigos.length)];
//
//            if (amigosSecretos.includes(amigo1) || amigosSecretos.includes(amigo2) || amigo1 == amigo2) {
//                continue;
//            }else{
//                amigosSecretos.push(amigo1, amigo2);
//                console.log(`${amigo1} -> ${amigo2}`);
//                listaSorteados.innerHTML  += `<p id="lista-sorteio">${amigo1} --> ${amigo2}</p>`
//            }
//        }
//    }
//}

