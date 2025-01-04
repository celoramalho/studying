from modelos.restaurante import Restaurante

def main():
    restaurante_subuai = Restaurante('subuai', 'fast food')
    restaurante_osteria = Restaurante('74 Osteria', 'Osteria')
    restaurante_burger_ting = Restaurante('Burger Ting', 'Fast Food')
    restaurante_niniuta = Restaurante('Niniuta', 'Gourmet')
    
    
    restaurante_osteria.receber_avaliacao('Spiga', 5)
    restaurante_osteria.receber_avaliacao('Alice', 5)
    restaurante_osteria.receber_avaliacao('Fernando', 4)
    
    restaurante_burger_ting.receber_avaliacao('Luan', 3)
    restaurante_burger_ting.receber_avaliacao('Ronan', 2)
    restaurante_burger_ting.receber_avaliacao('Spiga', 120)
    
    restaurante_niniuta.receber_avaliacao('Romulo', 5)
    
    restaurante_subuai.alterar_estado()


    print(Restaurante.listar_restaurantes())


if __name__ == '__main__':
    main()