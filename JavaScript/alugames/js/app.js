function alterarStatus(id) {
    let game = document.getElementById(`game-${id}`);
    let img = game.querySelector('.dashboard__item__img');
    let linkAlugar = game.querySelector('.dashboard__item__button');

    if (linkAlugar.classList.contains('dashboard__item__button--return')){
        img.classList.remove('dashboard__item__img--rented');
        linkAlugar.classList.remove('dashboard__item__button--return');
        linkAlugar.textContent = 'Alugar';
    }
    else{
        img.classList.add('dashboard__item__img--rented');
        linkAlugar.classList.add('dashboard__item__button--return');
        linkAlugar.textContent = 'Devolver';
    }
}