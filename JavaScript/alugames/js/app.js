function alterarStatus(id) {
    let game = document.getElementById(`game-${id}`);
    let img = game.querySelector('.dashboard__item__img');
    let link_alugar = game.querySelector('.dashboard__item__button');

    if (link_alugar.classList.contains('dashboard__item__button--return')){
        img.classList.remove('dashboard__item__img--rented');
        link_alugar.classList.remove('dashboard__item__button--return');
        link_alugar.textContent = 'Alugar';
    }
    else{
        img.classList.add('dashboard__item__img--rented');
        link_alugar.classList.add('dashboard__item__button--return');
        link_alugar.textContent = 'Devolver';
    }
}