class Personagem:
    def __init__(self,name,idade,xp):
        self.name=name
        self.idade=idade
        self.xp=xp
        print(f'O nome do seu personagem é {self.name}, possui {self.idade} anos e {self.xp} de xp')
    
    def xpcalculo(self):
        while True:
            print(f'Você possui {self.xp} de xp.')
            option=input("Quer adicionar ou remover o xp[A/R]?Se não desejar nenhuma das duas aperte N.")
            if option in'Aa':
                xp2=int(input("Digite o quanto você quer adicionar:"))
                self.xp=xp2+self.xp
                print(f'O seu personagem ficou com {self.xp} de xp.')
            elif option in 'Rr':
                xp2=int(input("Digite o quanto você quer remover:"))
                self.xp=self.xp-xp2
                print(f'O seu personagem ficou com {self.xp}')
            elif option in 'Nn':
                break

def ataque():
    import random
    dado=random.randrange(0,100)
    atributo=int(input("Digite o quanto você possui de atributo:"))
    pericia=int(input("Digite o quanto você possui de pericia:"))
    defense=int(input("Digite a porcentagem de chance do inimigo:"))
    attacktotal=(atributo+pericia+50)-defense
    if dado>attacktotal:
        print(f'Você falhou no seu ataque.O resultado no dado foi de {dado}')
    else:
        print(f'AI!Você acertou!O resultado no dado foi de {dado}')

    
def defesa():
    import random
    dado2=random.randrange(0,100)
    atributo2=int(input("Digite o quanto você possui de atributo:"))
    pericia2=int(input("Digite o quanto você possui de pericia:"))
    attack2=int(input("Digite a porcentagem de chance do inimigo:"))
    defesatotal=(attack2+50)-(pericia2+atributo2)
    if dado2>defesatotal:
        print(f'AI!Você defendeu o golpe!O resultado no dado foi de {dado2}')
    else:
        print(f'Você falhou na sua defesa.O resultado no dado foi de {dado2}')

def apresentaçao(self):
    print(f'Seu nome é {self.name}, sua idade é {self.idade} e atualmente você possui {self.xp} de xp.')
