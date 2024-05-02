import streamlit as st
from unidecode import unidecode
from dict_generos import generos_dict

# Função para remover acentos
def remover_acentos(palavra):
   return unidecode(palavra)

# Função para gerar um link a partir de um gênero
def gerar_link(genero_link):
    base_url = "https://www.mydoramas.com/genero/"
    link_com_genero = base_url + genero_link.replace(" ", "-")
    return link_com_genero


# Função para definir o estilo de fundo
def set_background(style):
    if style == 'blue':
        background_color = '#e6f7ff'  # Azul claro
    else:
        background_color = '#ffffff'  # Branco
        
    # Definindo o estilo da página
    st.markdown(
        f"""
        <style>
        .reportview-container {{
            background-color: {background_color};
            background-image: url("https://example.com/your_image.jpg");  /* Substitua pela URL da sua imagem de fundo */
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Função principal do aplicativo Streamlit
def main():
    # Definindo o estilo de fundo
    set_background('blue')

    escolha = st.sidebar.selectbox(
        "Escolha uma opção:",
        ["Gêneros", "Link do site", "Sair"]
    )

    if escolha == "Gêneros":
        st.subheader("Escolha uma ou mais opções de gênero:")
        opcoes_generos = list(generos_dict.values())
        escolha_genero = st.multiselect("Selecione os gêneros desejados:", opcoes_generos)
        
        if st.button("Pesquisar"):
            generos_validos = [genero for genero, valor in generos_dict.items() if valor in escolha_genero]
            if len(generos_validos) == 0:
                st.error('Erro: Nenhum gênero reconhecido. Tente novamente.')
            else:
                for genero_valido in generos_validos:
                    link_genero = gerar_link(genero_valido.lower())
                    st.write(link_genero)

    elif escolha == "Link do site":
        st.write("https://www.mydoramas.com/generos/")
        
if __name__ == "__main__":
    main()
