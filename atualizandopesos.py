import numpy as np
#and
entradas = np.array([[0,0],[0,1],[1,0],[1,1]])
saida = np.array([0,0,0,1])#saida esperada
#entradas = np.array([[0,0],[0,1],[1,0],[1,1]])
#saida = np.array([0, 1, 1, 1])

#
# entradas = np.array([[0,0],[0,1],[1,0],[1,1]])
# saida = np.array([0, 1, 1, 0])
pesos = np.array([0.0,0.0])
taxaAprendizagem =0.1
from time import  sleep
def calculaSaida(registro):
     s = registro.dot(pesos)
     return  ativacao(s)

def ativacao(resultado):
    if resultado >= 1:
        return 1
    return 0

calc = 0
def treinar():#ajuste de pesos
    erroTotal =1
    while(erroTotal != 0):
        erroTotal = 0
        for i in range(len(saida)):
            saidaCalculada =  calculaSaida(np.array(entradas[i]))
            erro = abs(saida[i] - saidaCalculada)
            erroTotal+= erro
            #atualizar 
            for j in range(len(pesos)):
                pesos[j] = pesos[j] + (taxaAprendizagem * entradas[i][j]* erro)
                print("peso atualizados%s"%pesos[[j]])
                #sleep(5)
            print("\n total de erros %s"%erroTotal)


if __name__ == '__main__':
    treinar()
    print("Rede Treinada")
    for i in np.arange(len(entradas)):
        c = calculaSaida(entradas[i])
        print(c)