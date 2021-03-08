from menu import*
from time import sleep
from personagem import*
import random
print('-'*30)
print('DAEMON RPG'.center(30))
print('-'*30)
sleep(1)
#Aqui fica o inicio do programa
while True:
    try:
        menu()
        option=int(input("Digite uma opção:"))
        print=''
        if option==1:
            name=input('Digite o nome do seu personagem:')
            idade=int(input('Digite a idade do seu personagem:'))
            xp=int(input('Digite o quanto de xp tem seu personagem:'))
            p1=Personagem(name,idade,xp)
        elif option==2:
            p1.xpcalculo()
        elif option==3:
            opçao=input("ATAQUE OU DEFESA?")
            if opçao in "ATAQUEataque":
                ataque()
            elif opçao in "DEFESAdefesa":
                defesa()
        elif option==4:
            break
    except ValueError:
        print('')
        print("Digite uma opção válida")
        print('')
    except KeyboardInterrupt:
        print('')
        print("O programa foi parado pelo usuário")
        print('')
