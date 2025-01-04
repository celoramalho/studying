from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

def main():
    restaurante_subuai = Restaurante('subuai', 'fast food')
    restaurante_osteria = Restaurante('74 Osteria', 'Osteria')
    restaurante_burger_ting = Restaurante('Burger Ting', 'Fast Food')
    restaurante_niniuta = Restaurante('Niniuta', 'Gourmet')
    
    
    bebida_coquinha_gelada = Bebida('Coquinha Gelada', 5.0, 'grande')
    bebida_vinho_lagar = Bebida('Vinho Branco Lagar', 64.0, 'grande')
    prato_risoto_limao_polvo = Prato('Risoto de limão com Polvo', 125, 'Risoto de limão siciliano com Polvo grelhado')
    
    restaurante_osteria.adicionar_item_no_cardapio(bebida_vinho_lagar)
    restaurante_osteria.adicionar_item_no_cardapio(bebida_coquinha_gelada)
    restaurante_osteria.adicionar_item_no_cardapio(prato_risoto_limao_polvo)
    
    
    restaurante_osteria.receber_avaliacao('Spiga', 5)
    restaurante_osteria.receber_avaliacao('Alice', 5)
    restaurante_osteria.receber_avaliacao('Fernando', 4)
    
    restaurante_burger_ting.receber_avaliacao('Luan', 3)
    restaurante_burger_ting.receber_avaliacao('Ronan', 2)
    restaurante_burger_ting.receber_avaliacao('Spiga', 120)
    
    restaurante_niniuta.receber_avaliacao('Romulo', 5)
    
    restaurante_subuai.alterar_estado()


    print(Restaurante.listar_restaurantes())
    restaurante_osteria.listar_cardapio()

if __name__ == '__main__':
    main()