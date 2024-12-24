resetQuantidade();

function resetQuantidade(){
    let inputQuantidade = document.getElementById('quantidade');
    inputQuantidade.value = 1;
}

function adicionarProdutoAoCarrinho(produto, quantidade) {
    let listaProduto = document.getElementById('lista-produtos');
    let valor = produto.split('-')[1];
    let nomeProduto = produto.split('-')[0];
    
    if (quantidade <= 0){
        alert('Quantidade deve ser maior que zero para adicionar ao carrinho');
        return;
    }else{
        listaProduto.innerHTML += `
        <section class="carrinho__produtos__produto">
          <span class="texto-azul">${quantidade}x</span> ${nomeProduto} <span class="texto-azul"> ${valor}</span>
        </section>
        `;
        somarValorTotal(valor, quantidade);
    }
}

function somarValorTotal(valor, quantidade) {
    let valorTotal = document.getElementById('valor-total')
    let valorAtual = valorTotal.textContent.split('$')[1];
    let valorProduto = valor.split('$')[1];

    let novoValor = parseInt(valorAtual) + parseInt(valorProduto)*parseInt(quantidade);
    console.log(valorAtual);
    console.log(novoValor);
    valorTotal.textContent = `R$${novoValor}`;
}

function adicionar() {
    let produto = document.getElementById('produto').value;
    let quantidade = document.getElementById('quantidade').value;

    console.log(`Produto: ${produto}`);
    console.log(`Quantidade: ${quantidade}`);

    adicionarProdutoAoCarrinho(produto, quantidade);
}
function limpar() {
    let listaProduto = document.getElementById('lista-produtos');
    let valorTotal = document.getElementById('valor-total');

    listaProduto.innerHTML = '';
    valorTotal.textContent = 'R$0';
    resetQuantidade();
}