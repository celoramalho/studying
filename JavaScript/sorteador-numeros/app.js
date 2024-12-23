function sortear() {
    let quantidade = parseInt(document.getElementById('quantidade').value)
    let doNumero = parseInt(document.getElementById('de').value)
    let ateNumero = parseInt(document.getElementById('ate').value)

    if (validaInputs(quantidade, doNumero, ateNumero)){
        pass
    }else{
        return
    }

    console.log(`Quantidade: ${quantidade}`);
    console.log(`Do número: ${doNumero}`);
    console.log(`Até o número: ${ateNumero}`);

    let numerosSorteados = [];
    while (numerosSorteados.length < quantidade) {
        numeroSorteado = obterNumerosSorteados(doNumero, ateNumero);
        if (numerosSorteados.includes(numeroSorteado)) {
            continue;
        }else{
            console.log(`numeroSorteado: ${numeroSorteado}`);
            numerosSorteados.push(numeroSorteado);
        }
    }
    exibirNaTela('#resultado', numerosSorteados);
    document.getElementById('btn-reiniciar').removeAttribute('disabled');
}

function validaInputs(quantidade, doNumero, ateNumero) {
    if  (doNumero > ateNumero)  {
        alert('Número mínimo do sorteio deve ser menor que o número máximo');
        return false;
    }else if (quantidade > ateNumero - doNumero) {
        alert('Quantidade de números sorteados deve ser menor que o número máximo - número mínimo');
        return false;
    }else{
        return true;
    }
}

function obterNumerosSorteados(min, max) {
    let numeroSorteado = parseInt(Math.random() * (max - min) + min);   
    return numeroSorteado;
}

function exibirNaTela(id, texto) {
    let campo = document.querySelector(id);
    campo.innerHTML = texto;
}

function reiniciar() {
    exibirNaTela('#resultado', 'Números sorteados:  nenhum até agora');
    document.getElementById('btn-reiniciar').setAttribute('disabled', true);
    document.getElementById('btn-sortear').removeAttribute('disabled');
}