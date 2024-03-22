import streamlit as st

# Definindo o título e ícone da página
st.set_page_config(
    page_title="Análise de Inadimplência",
    page_icon="🪙"
)

def main():
    st.title("Bem-vindo à Previsão de Inadimplência 📊")
    st.write(
        """
        Esta é uma aplicação de previsão de inadimplência desenvolvida com Streamlit.
        Aqui você pode inserir os dados do cliente e obter uma previsão sobre se é recomendado
        ou não disponibilizar crédito para esse cliente com base em uma análise de dados.
        """
    )
if __name__ == "__main__":
    main()