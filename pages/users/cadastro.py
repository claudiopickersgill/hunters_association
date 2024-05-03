import streamlit as st
import pandas as pd
from pages.conexao import conexao
import random
import string


def busca_tabela():
    worksheet_hunters, worksheet_guilds = conexao.faz_conexao()
    return worksheet_hunters, worksheet_guilds


worksheet_hunters, worksheet_guilds = busca_tabela()

# Function to find the last filled row in the worksheet.


def find_last_filled_row(worksheet):
    return len(worksheet.get_all_values()) + 1

# Function to insert data into the Google Sheet after the last filled row.


def insert_data_into_sheet(dataframe, table):
    # worksheet = worksheet_raw.get_worksheet(0)  # Replace 0 with the index of your desired worksheet
    values = dataframe.values.tolist()

    # Find the last filled row
    if table == 'hunters':
        last_filled_row_hunters = find_last_filled_row(worksheet_hunters)
    else:
        last_filled_row_guilds = find_last_filled_row(worksheet_guilds)

    # Insert the data after the last filled row
    if table == 'hunters':
        worksheet_hunters.insert_rows(values, last_filled_row_hunters)
    else:
        worksheet_guilds.insert_rows(values, last_filled_row_guilds)


def gerar_login(tamanho=8):
    caracteres = string.ascii_letters + string.digits
    login = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return login


def gerar_senha(tamanho=8):
    caracteres = string.ascii_letters + string.digits
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha


def individual():
    nome = st.text_input("Nome:", key="nome")
    sobrenome = st.text_input("Sobrenome:", key="sobrenome")
    classe = st.text_input("Classe:", key="classe")
    rank = st.text_input("Rank:", key="key")
    guilda = st.text_input(
        "Guilda: (caso não tenha, não preencher)", key="guilda")
    login = gerar_login()
    senha = gerar_senha()

    nova_linha = pd.DataFrame({'nome': [nome], 'sobrenome': [sobrenome], 'classe': [
                              classe], 'rank': [rank], 'guilda': [guilda], 'login': [login], 'senha': [senha]})

    if st.button("Finalizar Cadastro"):
        # Call the function to insert data into the Google Sheet
        insert_data_into_sheet(nova_linha, table='hunters')
        st.success("Cadastro Concluido com Sucesso")
        st.write("Novo login gerado:", login)
        st.write("Nova senha gerada:", senha)
        st.write("FAVOR ANOTAR LOGIN E SENHA. ELES NÃO APARECERAM NOVAMENTE")
        st.write("Obrigado por se cadastrar na Associação dos Caçadores. Acesse o painel LOGIN para verificar suas informações")


def guilda():
    nome_guilda = st.text_input("Nome da Guilda:", key="nome_guilda")
    presidente_guilda = st.text_input(
        "Presidente da Guilda:", key="presidente_guilda")
    rank_guilda = st.text_input("Rank da Guilda:", key="rank_guilda")
    associados_guilda = st.text_input(
        "Número de Asssociados:", key="associados_guilda")
    login = gerar_login()
    senha = gerar_senha()

    nova_linha = pd.DataFrame({'nome_guilda': [nome_guilda], 'presidente_guilda': [presidente_guilda], 'rank_guilda': [
                              rank_guilda], 'associados_guilda': [associados_guilda], 'login': [login], 'senha': [senha]})

    if st.button("Finalizar Cadastro"):
        # Call the function to insert data into the Google Sheet
        insert_data_into_sheet(nova_linha, table=None)
        st.success("Cadastro Concluido com Sucesso")
        st.write("Novo login gerado:", login)
        st.write("Nova senha gerada:", senha)
        st.write("FAVOR ANOTAR LOGIN E SENHA. ELES NÃO APARECERAM NOVAMENTE")
        st.write("Obrigado por cadastrar sua Guilda na Associação dos Caçadores. Acesse o painel LOGIN para verificar suas informações")
