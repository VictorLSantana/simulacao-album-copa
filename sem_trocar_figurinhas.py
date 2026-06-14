
from album import Album
import matplotlib.pyplot as plt 

PESSOAS_COLECIONANDO_ALBUM = 10_000

# Quantos pacotes foram necessários comprar para completar o album
qntd_pacotes = [] 

# Simulando pessoas colecionando o album
for i in range(PESSOAS_COLECIONANDO_ALBUM):
    pessoa = Album()

    contador = 0

    while 0 in pessoa.figurinhas_do_album:
        pacote = pessoa.pacote()
        pessoa.colar_figurinha(pacote)
        contador += 1

    qntd_pacotes.append(contador)
    
# Montando o gráfico
plt.hist(qntd_pacotes)
plt.title("Histograma de Álbuns Completos \n (sem trocar figurinha)")
plt.xlabel("Quantidade de Pacotes")
plt.ylabel("Quantidade de Pessoas")
plt.show()

