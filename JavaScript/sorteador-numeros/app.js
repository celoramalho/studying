function sortear() {
    let quantidade = parseInt(document.getElementById('quantidade').value)
    let doNumero = parseInt(document.getElementById('de').value)
    let ateNumero = parseInt(document.getElementById('ate').value)

    console.log(`Quantidade: ${quantidade}`);
    console.log(`Do número: ${doNumero}`);
    console.log(`Até o número: ${ateNumero}`);

    let numerosSorteados = [];

    while (numerosSorteados.length < quantidade) {
        let numeroSorteado = parseInt(Math.random() * (ateNumero) + doNumero);
        if (numerosSorteados.includes(numeroSorteado)) {
            continue
        }else{
            console.log(`numeroSorteado: ${numeroSorteado}`);
            numerosSorteados.push(numeroSorteado);
        }
    }
    exibirNaTela('#resultado', numerosSorteados);
    document.getElementById('btn-reiniciar').removeAttribute('disabled');
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