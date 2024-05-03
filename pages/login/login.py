import streamlit as st
import pandas as pd
from pages.conexao import conexao
from pages.visualizar import visual

worksheet_hunters, worksheet_guilds = conexao.faz_conexao()
hunters_login = worksheet_hunters.col_values(6)
hunters_password = worksheet_hunters.col_values(7)
guilds_login = worksheet_guilds.col_values(5)
guilds_password = worksheet_guilds.col_values(6)


def verify():
    # Username and password input fields
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # Login button
    login = None
    user_name = None
    user_type = None
    if st.button("Login"):
        # Check if username exists and password is correct
        if username in hunters_login:
            index_h = hunters_login.index(username)
            if hunters_password[index_h] == password:
                # st.write(worksheet_hunters.row_values(index_h+1)[0])
                st.success("Login Bem sucedido!")
                st.write(
                    f"Bem-Vindo, {worksheet_hunters.row_values(index_h+1)[0]}!")
                st.write("Aguarde! Estamos buscando seus dados.")
                login = True
                user_name = worksheet_hunters.row_values(index_h+1)[0]
                user_type = "hunter"
        elif username in guilds_login:
            index_g = guilds_login.index(username)
            if guilds_password[index_g] == password:
                # st.write(worksheet_guilds.row_values(index_g+1)[0])
                st.success("Login Bem sucedido!")
                st.write(
                    f"Bem-Vindo, {worksheet_guilds.row_values(index_g+1)[0]}!")
                st.write("Aguarde! Estamos buscando seus dados.")
                login = True
                user_name = worksheet_guilds.row_values(index_g+1)[0]
                user_type = "guilda"
        else:
            st.error("Nome de usuário ou password inválidos. Tente novamente.")
            login = False

    return login, user_name, user_type


def login():
    st.title("Login System")

    check, user_name, user_type = verify()

    if check == True:
        visual.visual(user_name, user_type)
