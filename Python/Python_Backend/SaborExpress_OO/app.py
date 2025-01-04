from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

def main():
    restaurante_subuai = Restaurante('subuai', 'fast food')
    restaurante_osteria = Restaurante('74 Osteria', 'Osteria')
    restaurante_burger_ting = Restaurante('Burger Ting', 'Fast Food')
    restaurante_niniuta = Restaurante('Niniuta', 'Gourmet')
    
    
    
    bebida_vinho_lagar = Bebida('Vinho Branco Lagar', 64.0, 'grande')
    prato_risoto_limao_polvo = Prato('Risoto de limão com Polvo', 125, 'Risoto de limão siciliano com Polvo grelhado')
    
    
    restaurante_osteria.receber_avaliacao('Spiga', 5)
    restaurante_osteria.receber_avaliacao('Alice', 5)
    restaurante_osteria.receber_avaliacao('Fernando', 4)
    
    restaurante_burger_ting.receber_avaliacao('Luan', 3)
    restaurante_burger_ting.receber_avaliacao('Ronan', 2)
    restaurante_burger_ting.receber_avaliacao('Spiga', 120)
    
    restaurante_niniuta.receber_avaliacao('Romulo', 5)
    
    restaurante_subuai.alterar_estado()


    print(Restaurante.listar_restaurantes())
    print(bebida_vinho_lagar, prato_risoto_limao_polvo, sep='\n')

if __name__ == '__main__':
    main()