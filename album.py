
import random

# Definindo algumas constantes
VALOR_PACOTE = 7 # valor do pacote de figurinhas em R$
QNTD_PACOTE = 7  # quantidade de figurinhas por pacote
QNTD_ALBUM = 980 # quantidade de figurinhas para completar o album

# Classe Album
class Album:
    def __init__(self):
        # O album é representado por um array com o tamanho da QNTD_ALBUM com todos
        # os elementos iguais a 0 inicialmente, o album vai sendo preenchido com a figurinha da posição
        # correspondente até ser totalmente completo. 
        self.figurinhas_do_album = [0 for f in range(QNTD_ALBUM)]
        self.figurinhas_repetidas = [] 
     
    # gerando 7 números aleatórios para simular as figurinhas que vem dentro de um pacote   
    def pacote(self):
        pacote = [random.randint(1, QNTD_ALBUM) for f in range(QNTD_PACOTE)]
        return pacote

    # recebe um pacote e verifica se as figurinhas já estão presente no album, não estiver
    # a figurinha é colada no album, caso contrário a figurinha é adicionada a lista de repetidas
    def colar_figurinha(self, pacote):
        for f in pacote:
            if self.figurinhas_do_album[f-1] == 0:
                self.figurinhas_do_album[f-1] = f
            else:
                self.figurinhas_repetidas.append(f)
                
    def trocar_figurinha(self, album1, album2):
        # conferindo se existe alguma figurinha que o album1 precisa que
        # esteja nas figurinhas repetidas do album2
        
        for f in album2.figurinhas_repetidas:
            if f in album1.figurinhas_do_album:
                continue
            else:
                # se existir a figurinha, o album1 cola a figurinha e o album2 remove a figurinha da lista de repetidas
                album1.colar_figurinha([f])
                album2.figurinhas_repetidas.remove(f)
                break

    
    
        
        
if __name__ == "__main__":
    album1 = Album()
    
    print(album1.figurinhas_do_album)
    
    meu_pacote = album1.pacote()
    
    print(meu_pacote)
    
    album1.colar_figurinha(meu_pacote)
    
    print(album1.figurinhas_do_album)
    print(album1.figurinhas_repetidas)
    