#Atividade 01: Criação de Threads
#Erick Gabriel Carvalho de Vasconcelos
#25114290013

#Passo 1: Criação da Biblioteca
import math
import time
import threading

#Obs: Este passo e bem importante para os seguintes tópicos
#Organização, Manutenção Facilitada, Modularidade


#Passo 2: Estrutura das Threads
def estrutura(nome, inicio, fim):
    for i in range (inicio, fim +1):
        print(f"{nome} > {i}")
time.sleep(1)

#Obs: Este passo serve para Executar tarefas simultâneas, Melhorar a performance e Evitar travamentos, 

#Sem threads: O programa fica travado enquanto o download acontece
#Com threads: O download acontece em segundo plano, e o usuário pode clicar nos botões, mexer na interface.


#Passo 3: Criação das Threads:
thread1 = threading.Thread(target=estrutura, args=("thread-1", 1, 10))
thread2 = threading.Thread(target=estrutura, args=("thread-2", 50, 60))

#Obs: Este passo é a criação das threads definitivamente, elas irão executar o programa da estrutura criada acima "estrutura" com seus respectivos tempos de intervalos e seus valores.


#Passo 4: Fazer com que as threads inicie a executar e rodar:
thread1.start()
thread2.start()

thread1.join()
thread2.join()

#Obs: Estes códigos são para a execução das threads.