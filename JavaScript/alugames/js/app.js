function alterarStatus(id) {
    let game = document.getElementById(`game-${id}`);
    let img = game.querySelector('.dashboard__item__img');
    let botao = game.querySelector('.dashboard__item__button');
    let nomeJogo =  game.querySelector('.dashboard__item__name');
    console.log(`Jogo: ${nomeJogo.textContent}`);

    if (botao.classList.contains('dashboard__item__button--return')){
        img.classList.remove('dashboard__item__img--rented');
        botao.classList.remove('dashboard__item__button--return');
        botao.textContent = 'Alugar';
    }
    else{
        img.classList.add('dashboard__item__img--rented');
        botao.classList.add('dashboard__item__button--return');
        botao.textContent = 'Devolver';
    }
}