resetar();

function comprar(){
    let tipoIngresso = document.querySelector('#tipo-ingresso').value;
    let quantidadeIngresso = document.querySelector('#qtd').value;

    if (quantidadeIngresso <= 0) {
        alert('Quantidade deve ser maior que 0');
    }

    console.log(`Tipo de ingresso: ${tipoIngresso}`);
    console.log(`Quantidade: ${quantidadeIngresso}`);
    alterarQuantidadeEstoque(tipoIngresso, quantidadeIngresso);

}

function alterarQuantidadeEstoque(tipoIngresso, quantidadeIngresso){
    let quantidadeEstoque = document.querySelector(`#qtd-${tipoIngresso}`);
    let novaQuantidade = parseInt(quantidadeEstoque.textContent) - parseInt(quantidadeIngresso);

    if (novaQuantidade < 0){
        alert(`Estoque insuficiente em ${tipoIngresso}`);
        return
    }else{
        if(novaQuantidade == 0){
            alterarBotaoCompra('disable');
        }
        alert(`Compra realizada com sucesso! ${quantidadeIngresso} ingressos ${tipoIngresso} comprados`);
        quantidadeEstoque.textContent = novaQuantidade;
    }
    alterarBotaoCompra('enable');    
}

function alterarBotaoCompra(status){
    let botao = document.querySelector('#botao-comprar');

    if (status == 'enable'){
        botao.classList.remove('botao-desabilitado');
        botao.removeAttribute('disabled');
    }else{
        botao.setAttribute('disabled', true);
        botao.classList.add('botao-desabilitado');
    }
}

function resetar(){
    let ingressoPista = document.querySelector('#qtd-pista').value;
    let ingressoSuperior = document.querySelector('#qtd-superior').value;
    let ingressoInferior = document.querySelector('#qtd-inferior').value;
    ingressoPista.textContent = 100;
    ingressoSuperior.textContent = 200;
    ingressoInferior.textContent = 400;
    alterarBotaoCompra('enable');
}
