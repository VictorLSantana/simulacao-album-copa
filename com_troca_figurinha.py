
from album import Album, VALOR_PACOTE
import matplotlib.pyplot as plt 

PESSOAS_COLECIONANDO_ALBUM = 1_000

# Quantos pacotes foram necessários comprar para completar o album
qntd_pacotes = [] 

# Simulando pessoas colecionando o album
for i in range(PESSOAS_COLECIONANDO_ALBUM):
    pessoa1 = Album()
    pessoa2 = Album()

    contador = 0

    while 0 in pessoa1.figurinhas_do_album or 0 in pessoa2.figurinhas_do_album:
        pacote = pessoa1.pacote()
        pessoa1.colar_figurinha(pacote)
        
        pacote = pessoa2.pacote()
        pessoa2.colar_figurinha(pacote)
        
        pessoa1.trocar_figurinha(pessoa1, pessoa2)
        pessoa2.trocar_figurinha(pessoa2, pessoa1)
        
        
        contador += 1

    qntd_pacotes.append(contador)
    print(i)

    
# Montando o gráfico
plt.hist(qntd_pacotes)
plt.title("Histograma de Álbuns Completos \n (trocando figurinhas)")
plt.xlabel("Quantidade de Pacotes")
plt.ylabel("Quantidade de Pessoas")
plt.savefig("graficos/hist_com_troca.png")
plt.show()


if __name__ == "__main__":
    print(f"Quantidade de colecionadores: {PESSOAS_COLECIONANDO_ALBUM}")
    print(f"Média de pacotes por colecionador: {sum(qntd_pacotes) / len(qntd_pacotes):.2f}")
    print(f"Mediana de pacotes por colecionador: {sorted(qntd_pacotes)[len(qntd_pacotes) // 2]}")
    print(f"Máximo de pacotes por colecionador: {max(qntd_pacotes)}")
    print(f"Mínimo de pacotes por colecionador: {min(qntd_pacotes)}")
    print(f"Valor médio gasto com pacotes: {sum(qntd_pacotes) / len(qntd_pacotes) * VALOR_PACOTE:.2f}")





