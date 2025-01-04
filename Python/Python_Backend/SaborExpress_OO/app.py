from modelos.restaurante import Restaurante

def main():
    restaurante_subuai = Restaurante('subuai', 'fast food')
    restaurante_osteria = Restaurante('74 Osteria', 'Osteria')
    restaurante_burger_ting = Restaurante('Burger Ting', 'Fast Food')
    restaurante_niniuta = Restaurante('Niniuta', 'Gourmet')

    restaurante_subuai.alterar_estado()


    print(Restaurante.listar_restaurantes())


if __name__ == '__main__':
    main()