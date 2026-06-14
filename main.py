
import random

# Definindo algumas constantes
VALOR_PACOTE = 7 # valor do pacote de figurinhas em R$
VALOR_ALBUM = 75 # valor do album de figurinhas em R$
QNTD_PACOTE = 7  # quantidade de figurinhas por pacote
QNTD_ALBUM = 10 # quantidade de figurinhas para completar o album

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

    def colar_figurinha(self, pacote):
        for f in pacote:
            if self.figurinhas_do_album[f-1] == 0:
                self.figurinhas_do_album[f-1] = f
            else:
                self.figurinhas_repetidas.append(f)

    
    
        
        
if __name__ == "__main__":
    album1 = Album()
    
    print(album1.figurinhas_do_album)
    
    meu_pacote = album1.pacote()
    
    print(meu_pacote)
    
    album1.colar_figurinha(meu_pacote)
    
    print(album1.figurinhas_do_album)
    print(album1.figurinhas_repetidas)
    