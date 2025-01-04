from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

def main():
    restaurante_subuai = Restaurante('subuai', 'fast food')
    restaurante_osteria = Restaurante('74 Osteria', 'Osteria')
    restaurante_burger_ting = Restaurante('Burger Ting', 'Fast Food')
    restaurante_niniuta = Restaurante('Niniuta', 'Gourmet')
    
    
    bebida_coquinha_gelada = Bebida('Coquinha Gelada', 5.0, 'grande')
    bebida_vinho_lagar = Bebida('Vinho Branco Lagar', 64.0, 'grande')
    bebida_coquinha_gelada.aplicar_desconto()
    prato_risoto_limao_polvo = Prato('Risoto de limão com Polvo', 125, 'Risoto de limão siciliano com Polvo grelhado')
    prato_risoto_limao_polvo.aplicar_desconto()
    meringata_di_fragola = Sobremesa('Meringata di Fragola', 43, 'Morangos assados, creme de chocolate branco, gelato de iogurte e suspiro de manjericão.', 'Dolci', 'grande')


    
    
    restaurante_osteria.adicionar_item_no_cardapio(bebida_vinho_lagar)
    restaurante_osteria.adicionar_item_no_cardapio(bebida_coquinha_gelada)
    restaurante_osteria.adicionar_item_no_cardapio(prato_risoto_limao_polvo)
    restaurante_osteria.adicionar_item_no_cardapio(meringata_di_fragola)
    
    
    restaurante_osteria.receber_avaliacao('Spiga', 5)
    restaurante_osteria.receber_avaliacao('Alice', 5)
    restaurante_osteria.receber_avaliacao('Fernando', 4)
    
    restaurante_burger_ting.receber_avaliacao('Luan', 3)
    restaurante_burger_ting.receber_avaliacao('Ronan', 2)
    restaurante_burger_ting.receber_avaliacao('Spiga', 120)
    
    restaurante_niniuta.receber_avaliacao('Romulo', 5)
    
    restaurante_subuai.alterar_estado()


    print(Restaurante.listar_restaurantes())
    restaurante_osteria.exibir_cardapio

if __name__ == '__main__':
    main()