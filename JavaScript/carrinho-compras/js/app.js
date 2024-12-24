resetQuantidade();

function resetQuantidade(){
    let inputQuantidade = document.getElementById('quantidade');
    inputQuantidade.value = 1;
}

function adicionarProdutoAoCarrinho(produto, quantidade) {
    let listaProduto = document.getElementById('lista-produtos');
    let valorUnitario = produto.split(' - ')[1];
    let nomeProduto = produto.split('-')[0];
    let produtosAdicionados = document.querySelectorAll('.carrinho__produtos__produto');
    
    if (quantidade <= 0){
        alert('Quantidade deve ser maior que zero para adicionar ao carrinho');
        return;
    }else{
        if (listaProduto.innerHTML.includes(nomeProduto)){
            for (let i = 0; i < produtosAdicionados.length; i++) {
                if (produtosAdicionados[i].innerHTML.includes(nomeProduto)) {
                    let campoQuantidade = produtosAdicionados[i].getElementsByTagName('span')[0];
                    let quantidadeAtual = campoQuantidade.textContent.split('x')[0];
                    let quantidadeNova = parseInt(quantidade) + parseInt(quantidadeAtual);
                    console.log(`quantidadeAtual: ${quantidadeAtual},quantidadeNova: ${quantidadeNova}`);
                    campoQuantidade.textContent = `${quantidadeNova}x`;
                }
            }
        }
        else{
            listaProduto.innerHTML += `
            <section class="carrinho__produtos__produto">
            <span class="texto-azul">${quantidade}x</span> ${nomeProduto} <span class="texto-azul"> ${valorUnitario}</span>
            </section>
            `;
        }
        somarValorTotal(valorUnitario, quantidade);
    }
}

function somarValorTotal(valorUnitario, quantidade) {
    let valorTotal = document.getElementById('valor-total')
    let valorAtual = valorTotal.textContent.split('$')[1];
    let valorProduto = valorUnitario.split('$')[1];

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
//(?<![\w-])valorUnitario(?![\w-])
