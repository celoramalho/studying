function comprar(){
    let tipoIngresso = document.querySelector('#tipo-ingresso').value;
    let quantidadeIngresso = document.querySelector('#qtd').value;

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
            alterarBotaoCompra();
        }
        alert(`Compra realizada com sucesso! ${quantidadeIngresso} ingressos ${tipoIngresso} comprados`);
        quantidadeEstoque.textContent = novaQuantidade;
    }    
}

function alterarBotaoCompra(){
    let botao = document.querySelector('#botao-comprar');
    botao.setAttribute('disabled', true);
    botao.classList.add('botao-desabilitado');
}