import streamlit as st
from pages.principal import principal
from pages.users import associar
from pages.mapas import maps
from pages.login import login

st.set_page_config(layout="wide")

# Menu lateral
st.sidebar.title("Menu")
menu = st.sidebar.selectbox('Selecione uma Página', [
    'Principal', "Associar-se", "Login", "Portais"])

if menu == 'Principal':
    principal.principal()
elif menu == 'Associar-se':
    associar.associar()
elif menu == 'Login':
    login.login()
elif menu == "Portais":
    maps.maps()
