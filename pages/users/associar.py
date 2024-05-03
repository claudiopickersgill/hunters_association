import streamlit as st
from pages.users import cadastro


def associar():

    st.markdown("<div style='text-align: center;'> <img src='https://i.ibb.co/BNpHYqX/HA-Logo.jpg' alt='HA-Logo' width='300' height='300' border='0' > </div>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: grey;'>Bem-vindo a Pagina de Associação</h3>",
                unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: grey;'>Selecione Abaixo o Tipo de Associação</h3>",
                unsafe_allow_html=True)
    st.divider()
    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("<h4 style='text-align: center; color: silver;'>Caçador Individual<h4>",
                    unsafe_allow_html=True)
        st.markdown("<div style='text-align: center;'> <img src='https://i.ibb.co/xg98RNs/ca-ador.jpg' alt='Caçador' width='150' height='150' border='0' > </div>", unsafe_allow_html=True)

    with col2:
        option = st.selectbox('Como Gostaria De Se Associar?',
                              ('Selecione', 'Caçador Individual', 'Guilda'))

        if option == "Caçador Individual":
            st.write("Digite os Dados Cadastrais:")
            cadastro.individual()
        elif option == "Guilda":
            st.write("Digite os Dados Cadastrais:")
            cadastro.guilda()

    with col3:
        st.markdown("<h4 style='text-align: center; color: silver;'>Guilda<h4>",
                    unsafe_allow_html=True)
        st.markdown("<div style='text-align: center;'> <img src='https://i.ibb.co/SVRgQLn/guilda.jpg' alt='HA-Logo' width='150' height='150' border='0' > </div>", unsafe_allow_html=True)

    st.divider()
    st.divider()
