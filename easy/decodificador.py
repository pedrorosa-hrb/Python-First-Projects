import random
import time
from funcoes import divisoria,printsp

# \033[0;32;47m \033[m



letras1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z']
letras2 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']
nums1 = []
nums2 = []

for _ in range(2):
    nums1.append(random.choice(range(224)))
    nums2.append(random.choice(range(99)))

while True:
    divisoria()
    printsp("Olá oque deseja fazer?")
    printsp("(1) Codificar/decodificar (2) Sair")
    divisoria()

    try:
        esc = int(input())
    except (ValueError,TypeError):
        divisoria()
        printsp("O tipo de dado que você digitou não pode ser usado!")
        divisoria()
    
    if esc == 1:
        divisoria()
        printsp("Ok! Digite a string que deseja codificar:")
        str_deco = str(input("-> "))
        divisoria()

        text_to_code = []
        text_to_code2 = []
        for _ in range(3):
            text_to_code.append(random.choice(letras1))
            text_to_code2.append(random.choice(letras2))
        str_all = "".join(map(str,text_to_code)) + "".join(map(str,nums1)) + "".join(map(str,nums2)) + "".join(map(str,text_to_code2))

        str_code = list(str_all)
        random.shuffle(str_code)
        str_code = "".join(str_code)
        divisoria()
        printsp(f'Seu texto codificado é : {str_code}')
        divisoria()
        printsp("O que deseja fazer?")
        printsp("(1) Decodificar seu texto (2) Sair")
        divisoria()

        try:
            esc2 = int(input())
        except (ValueError,TypeError):
            divisoria()
            printsp("O tipo de dado que você digitou não pode ser usado!")
            divisoria()
        
        if esc2 == 2:
            divisoria()
            printsp("Saindo. . .")
            divisoria()

            time.sleep(1)

            break
        elif esc2 == 1:
            divisoria()
            printsp(f'O seu texto decodificado é {str_deco}')
            divisoria()
        else:
            divisoria()
            printsp("Digite (1) ou (2)")
            divisoria()
        break
    elif esc == 2:
        divisoria()
        printsp("Saindo. . .")
        divisoria()

        time.sleep(1)
        break
    else:
        divisoria()
        printsp("Digite (1) ou (2)")
        divisoria()

    
