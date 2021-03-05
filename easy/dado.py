import random
import time
from funcoes import divisoria,printsp

def dado_mostrar(dado):
    divisoria()
    print(f"\033[1;32;40mO número que você tirou foi \033[m\033[1;97;40m{dado}\033[m")
    divisoria()

while True:
    divisoria()
    printsp("Olá , escolha um valor de dado para rodar:")
    printsp("(6) (8) (16) (32) - (0) SAIR")
    
    try:
        esc_dado = int(input("\033[1;32;40m-> \033[m"))
    except (ValueError,TypeError): 
        divisoria()
        printsp("Digite um número!")
        divisoria()

    divisoria()

    if esc_dado == 6:
        dado = random.choice(range(6))
        dado_mostrar(dado)
    elif esc_dado == 8:
        dado = random.choice(range(8))
        dado_mostrar(dado)
    elif esc_dado == 16:
        dado = random.choice(range(16))
        dado_mostrar(dado)
    elif esc_dado == 32:
        dado = random.choice(range(32))
        dado_mostrar(dado)            
    elif esc_dado == 0:
        divisoria()
        printsp("Saindo. . .")
        divisoria()

        time.sleep(1)
        break
    else:
        divisoria()
        printsp("Digite um número valido!")
        divisoria()