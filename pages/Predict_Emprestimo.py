import streamlit as st
import requests
import pandas as pd
import json


def predict_emprestimo(data):
    print('Fazendo a requisição!!!')
    url = 'https://predict-emprestimo.onrender.com/empresa/predict'
    header = {'Content-type': 'application/json' }
    r = requests.post( url, data=data, headers=header )
    print( 'Status Code {}'.format( r.status_code ) )
    prediction = r.json()[0]['prediction']
    print(prediction)
    return prediction


# Configurando a página do Streamlit
st.set_page_config(
    layout="wide",
    page_title="Previsão de Inadimplência 📊",
    page_icon="📊"
)


st.title("Previsão de Inadimplência 📊")

col1, col2, col3, col4 = st.columns(4)

with col1:
    idade = st.number_input('Insira a Idade do Cliente')

with col2:
    renda = st.number_input('Insira a Renda do Cliente')

with col3:
    tempo_emprego = st.number_input('Insira o Tempo de Emprego do Cliente')

with col4:
    valor_emprestimo = st.number_input('Insira o Valor do Empréstimo do Cliente')

col5, col6, col7, col8 = st.columns(4)
with col5:
    taxa_juros_emprestimo = st.number_input('Insira a taxa de Juros do Empréstimo')

with col6:
    #relacao_emprestimo_renda = st.number_input('Insira a Relação Empréstimo Renda')
    # Definindo o valor inicial e travando o campo de entrada
    # Verificando se tanto a renda quanto o valor do empréstimo são diferentes de zero
    if renda != 0 and valor_emprestimo != 0:
        # Calculando a relação empréstimo/renda
        valor_relacao_emprestimo_renda = int(valor_emprestimo)/int(renda) 
    else:
        # Definindo um valor padrão para evitar a divisão por zero
        valor_relacao_emprestimo_renda = 0

    # Definindo o campo de entrada com o valor calculado
    relacao_emprestimo_renda = st.text_input('Insira a Relação Empréstimo Renda', value=str(valor_relacao_emprestimo_renda), disabled=True, key='valor_relacao_emprestimo_renda')



with col7:
    historico_credito = st.number_input('Insira o Histórico de Crédito')

with col8:
    #posse_casa = st.text_input('Insira o Tipo de Posse de Casa')
    posse_casa = st.selectbox('Insira o Tipo de Posse de Casa', (['RENT', 'OWN', 'MORTGAGE', 'OTHER']))

col9, col10, col11 = st.columns(3)

with col9:
    #finalidade_emprestimo = st.text_input('Insira A Finalidade do Empréstimo')
    finalidade_emprestimo = st.selectbox(
    'Insira A Finalidade do Empréstimo',
    (['PERSONAL', 'EDUCATION', 'MEDICAL', 'VENTURE', 'HOMEIMPROVEMENT',
       'DEBTCONSOLIDATION']) )

with col10:
    #registro_inadimplencia = st.text_input('Possui Registro de Inadimplência?')
    registro_inadimplencia = st.selectbox(
    'Possui Registro de Inadimplência?',
    (['Y', 'N']) ) 
    

with col11:
    #grau_risco_emprestimo = st.text_input('Digite o Grau de Risco do Empréstimo')
    grau_risco_emprestimo = st.selectbox(
    'Digite o Grau de Risco do Empréstimo',
    (['D', 'B', 'C', 'A', 'E', 'F', 'G']) ) 

lista_dados = []
dict_data = {
    'idade': int(idade),
    'renda': renda,
    'tempo_emprego': float(tempo_emprego),
    'valor_emprestimo': int(valor_emprestimo),
    'taxa_juros_emprestimo': float(taxa_juros_emprestimo),
    'relacao_emprestimo_renda': float(relacao_emprestimo_renda),
    'historico_credito': int(historico_credito),
    'posse_casa': posse_casa,
    'finalidade_emprestimo': finalidade_emprestimo,
    'registro_inadimplencia': registro_inadimplencia,
    'grau_risco_emprestimo': grau_risco_emprestimo
}

# lista_dados.append(dict_data)
df = pd.DataFrame([dict_data])
data = json.dumps( df.to_dict( orient='records' ) )





if st.button('Previsão'):
    with st.spinner('Nosso Modelo de Inteligência Artificial Está Analisando os Dados....'):
        previsao = predict_emprestimo(data)
        if previsao != 0:
            st.markdown("<h4> <p style='color:red;'> Nosso modelo de Inteligência Artificial Recomenda a não disponibilização de crédito para esse cliente, pois ele possui uma alta probabilidade de inadimplência</p></h4>", unsafe_allow_html=True)
        else:
            st.markdown("<p style='color:green;'>### Nosso modelo de Inteligência Artificial Recomenda a disponibilização de crédito para esse cliente, pois ele possui uma baixa probabilidade de inadimplência </p>", unsafe_allow_html=True)




