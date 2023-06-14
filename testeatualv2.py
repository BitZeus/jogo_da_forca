#-------------------------------------------------------------------------------
#                           TESTE nº 1
#
# Curso: Fundamentos de Python
# UFCD/Módulo/Temática: UFCD: 10793 - Fundamentos de Python
# Ação: 10793_02/L
#
# Grupo 2
# Nome dos Formandos:   Andreia Martins
#                       Pedro Fragoso
#                       Ulisses Alvarinho
#
# Programa: Jogo da Forca
#-------------------------------------------------------------------------------

#inicio do programa


# Importação do módulo random para escolher uma palavra aleatória
import random

# Lista de palavras para o jogo da Forca
palavras = ["ajuda", "beato", "areeiro", "benfica", "alvalade", "marvila", "campolide", "lumiar", "olivais"]

# Escolha aleatória de uma palavra da lista palavras[] e guarda na variavel palavra_secreta
palavra_secreta = random.choice(palavras)

# Inicialização da lista de letras adivinhadas com o valor de "_" tendo em conta o tamanho da palavra_secreta
letras_adivinhadas = ["_"] * len(palavra_secreta)

# Número máximo de tentativas do jogador
max_tentativas = 5

#alfabeto=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#print(alfabeto)

#alfabeto=[]
#for i in range(97,123):
    #char = chr(i)
    #alfabeto.append(char)


#inicializa a lista alfabeto[] com os caracteres aceites pelo jogo. Dado que são nomes de cidades exclui tudo o que são numeros.     
alfabeto=[]
for i in range(65,91):  #adiciona as letras maiusculas do alfabeto segundo tabela ascii
    char = chr(i)
    alfabeto.append(char)
for i in range(97,123): #adiciona as letras minusculas do alfabeto segundo tabela ascii
    char = chr(i)
    alfabeto.append(char)
for i in range(192,256):  #adiciona as letras com acentuação/caracteres especiais do alfabeto segundo tabela ascii  
    char = chr(i)
    alfabeto.append(char)
    



# Função para desenhar o boneco da forca consoante as tentativas
def desenhar_boneco(tentativas):
    if tentativas == 0:
        print("    ____________________________________________________________")
        print("   |/                                                           |")
        print("   |                                            |               |               |    ")
        print("   |                                           ( )             _|_             ( )")
        print("   |                                          |   |     ___   |   |   ___     |   |")
        print("   |                                          |   |____|   |__|   |__|   |____|   | ")
        print("   |                                          |                                   |")
        print("   |                                          |               _____               | ")
        print("   |                                          |              |     |              |")
        print("   |                                                         |     |")
        print("   |                                                           ")
        print("   |                                                          ")
        print("   |                                                           ")
        print("___|___")
    elif tentativas == 1:
        print("    ____________________________________________________________")
        print("   |/                                                           |")
        print("   |                                            |               |               |")
        print("   |                                           ( )             _|_             ( )")
        print("   |                                          |   |     ___   |   |   ___     |   |")
        print("   |                                          |   |____|   |__|   |__|   |____|   |")
        print("   |                                          |                                   |")
        print("   |                                          |               _____               |")
        print("   |                                          |              |     |              |")
        print("   |                                          |              |     |              |")           
        print("   |                                          |              |_____|              |")
        print("   |                                          |                                   |")
        print("   |                                          |                                   |")
        print("   |                                          |                                   |")
        print("___|___")
    elif tentativas == 2:
        print("    ____________________________________________________________")
        print("   |/                                                           |")
        print("   |                                            |               |               |")
        print("   |                                           ( )             _|_             ( )")
        print("   |                                          |   |     ___   |   |   ___     |   |")
        print("   |                                          |   |____|   |__|   |__|   |____|   |")
        print("   |                                          |                                   |")
        print("   |                                          |               _____               |")
        print("   |                                          |              |     |              |")
        print("   |                                          |              |     |              |")           
        print("   |                                          |              |_____|              |")
        print("   |                                          |                                   |")
        print("   |                                          |       ____                        |")
        print("   |                                          |      |    |                       |")
        print("   |                                          |      |    |                       |")
        print("   |                                          |      |____|                       |")
        print("   |                                          |                                   |")
        print("   |                                          |                                   |")
        print("   |                                          |                                   |")
        print("   |                                          |                                   |")
        print("___|___")
    elif tentativas == 3:
        print("    ____________________________________________________________")
        print("   |/                                                           |")
        print("   |                                            |               |               |")
        print("   |                                           ( )             _|_             ( )")
        print("   |                                          |   |     ___   |   |   ___     |   |")
        print("   |                                          |   |____|   |__|   |__|   |____|   |")
        print("   |                                          |                                   |")
        print("   |                                          |               _____               |")
        print("   |                                          |              |     |              |")
        print("   |                                          |              |     |              |")           
        print("   |                                          |              |_____|              |")
        print("   |                                          |                                   |")
        print("   |                                          |       ____             ____       |")
        print("   |                                          |      |    |           |    |      |")
        print("   |                                          |      |    |           |    |      |")
        print("   |                                          |      |____|           |____|      |")
        print("   |                                          |                                   |")
        print("   |                                          |                                   |")
        print("   |                                          |                                   |          ____      ____      ____      ____")
        print("   |                                          |                                   |_________|    |____|    |____|    |____|    |")
        print("   |                                          |                                                                                |")
        print("   |                                          |                                                                                |")
        print("   |                                          |                                                                                |")   
        print("___|___")
    elif tentativas == 4:
       print("    ____________________________________________________________")
       print("   |/                                                           |")
       print("   |                                            |               |               |")
       print("   |                                           ( )             _|_             ( )")
       print("   |                                          |   |     ___   |   |   ___     |   |")
       print("   |                                          |   |____|   |__|   |__|   |____|   |")
       print("   |                                          |                                   |")
       print("   |                                          |               _____               |")
       print("   |                                          |              |     |              |")
       print("   |                                          |              |     |              |")           
       print("   |                                          |              |_____|              |")
       print("   |                                          |                                   |")
       print("   |                                          |       ____             ____       |")
       print("   |                                          |      |    |           |    |      |")
       print("   |                                          |      |    |           |    |      |")
       print("   |                                          |      |____|           |____|      |")
       print("   |                                          |                                   |")
       print("   |                                          |                                   |")
       print("   |                                          |                                   |          ____      ____      ____      ____")
       print("   |                                          |                                   |_________|    |____|    |____|    |____|    |")
       print("   |                                          |                                                                                |")
       print("   |                                          |                ____                                                            |")
       print("   |")
       print("___|___")
    else:
        print("    ____________________________________________________________")
        print("   |/                                                           |")
        print("   |                                            |               |               |")
        print("   |                                           ( )             _|_             ( )")
        print("   |                                          |   |     ___   |   |   ___     |   |")
        print("   |                                          |   |____|   |__|   |__|   |____|   |")
        print("   |                                          |                                   |")
        print("   |                                          |               _____               |")
        print("   |                                          |              |     |              |")
        print("   |                                          |              |     |              |")           
        print("   |                                          |              |_____|              |")
        print("   |                                          |                                   |")
        print("   |                                          |       ____             ____       |")
        print("   |                                          |      |    |           |    |      |")
        print("   |                                          |      |    |           |    |      |")
        print("   |                                          |      |____|           |____|      |")
        print("   |                                          |                                   |")
        print("   |                                          |                                   |")
        print("   |                                          |                                   |          ____      ____      ____      ____")
        print("   |                                          |                                   |_________|    |____|    |____|    |____|    |")
        print("   |                                          |                                                                                |")
        print("   |                                          |                ____                                                            |")
        print("   |                                          |               |    |                                                          /")
        print("   |                                          |               |    |                                                         /")   
        print("   |                                          |               |    |                                                        |")
        print("   |..........................................|               |    |                                                        |.................")
        print("___|___")

# Função principal do jogo
def jogo_forca():
    tentativas = 0
    letras_erradas = []
    #letras_adivinhadas = palavra_secreta[] #Acrescentei dicionário letras corretas

    print("Olá, bem-vindo ao jogo da Forca!")          
    print("Adivinha a palavra secreta.")
    print("Vamos dar-te uma dica, é uma das freguesias de Lisboa!")

    
    print("Palavra: ", " ".join(letras_adivinhadas)) # Exibe os espaços em branco para cada letra da palavra

    while tentativas < max_tentativas:
        letra = input("Digita uma letra: ").lower() #solicita uma letra ao jogador e converte para minuscula

        if letra in alfabeto and len(letra) == 1:   #verifica se o caractere existe na lista albeto[] e se é um unico caratere
            if letra in letras_adivinhadas or letra in letras_erradas: #Impedir a repetição de letras. PF
                print("Já digistaste essa letra, tente outra!")
                continue
            
            if letra in palavra_secreta:            # Verifica se a letra fornecida está presente na palavra secreta
                for i in range(len(palavra_secreta)):
                    if palavra_secreta[i] == letra:
                        letras_adivinhadas[i] = letra
                        print("Parabéns, acertaste numa letra!") #acrescentei Parabéns acertaste, na letra.PF
            else:
                letras_erradas.append(letra)        #adiciona a letra errada à lista letras_erradas[]
                tentativas += 1                     #incrementa o numero de tentativas já usadas
                desenhar_boneco(tentativas)         #Exibe o boneco de acordo com o nº de tentativas
        
            print("Palavra: ", " ".join(letras_adivinhadas))    # Atualizar a exibição da palavra com a letra revelada, se estiver correta

            
            if "_" not in letras_adivinhadas:                   # Verifica se o jogador venceu ou perdeu o jogo
                print("Parabéns!! Ganhaste \o/")
                return
        elif len(letra) == 1:                       #faz o print de erro se for um único caractere mas que não está na lista alfabeto[], ou seja, numeros
            print("Inválido. Apenas letras. Tenta novamente.")
        else:                                       #faz o print de erro se nenhuma das opções
            print("Inválido. Digita uma única letra por favor.")

        
        print("Letras erradas: ", ", ".join(letras_erradas)) # Solicita que o segundo jogador insira uma letra

    print("Oh, não conseguiste! A palavra secreta era:", palavra_secreta,".Tenta outra vez!")

# Iniciar o jogo da forca
jogo_forca()