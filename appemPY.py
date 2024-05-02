from unidecode import unidecode
from dict_generos import generos_dict


#FUNÇÕES

#função para retirar acentos  
#e caracteres especiais de uma string
def remover_acentos(palavra):
   return unidecode(palavra)

#função que gerar um link apartir de uma palavra
def gerar_link(genero_link):
    base_url = "https://www.mydoramas.com/generos/"
    link_com_genero = base_url + genero_link.replace(" ", "-")
    return link_com_genero





escolha = ""

while escolha != "0":
    escolha = input("""
        Webscrapping Doramas

        [1] - Gêneros
        [2] - Link do site
        [0] - Sair

        Escolha uma opção: """)

    if escolha == "1":
        generos_escolhidos = []
        while True:  
            print("""
            Escolha uma opção de gênero:
                
                - Animação 
                - Cinema 
                - Drama
                
                    """)
            entrada_generos = input("Digite os gêneros que deseja (separados por vírgula): ")
            generos_validos = [gen for gen in remover_acentos(entrada_generos) if gen in generos_dict]

            if len(generos_validos) == 0:
                print('Erro: Nenhum gênero reconhecido. Tente novamente.')
            else:
                generos_escolhidos.extend(generos_validos)
                escolha_continuar = input("Deseja escolher mais gêneros? (sim/não): ")
                if escolha_continuar.lower() != 'sim':
                    break

        for genero_escolhido in generos_escolhidos:
            link_genero = gerar_link(genero_escolhido)
            print(link_genero)

    elif escolha == "2":
        print("https://www.mydoramas.com/generos/")
    elif escolha == "0":
        print('Saiu do programa')
        break
