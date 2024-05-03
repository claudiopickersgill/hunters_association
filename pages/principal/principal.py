import streamlit as st
from pages.guildas import guildas


def principal():

    st.markdown("<div style='text-align: center;'> <img src='https://i.ibb.co/BNpHYqX/HA-Logo.jpg' alt='HA-Logo' width='300' height='300' border='0' > </div>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: grey;'>Bem-vindo a Associação dos Caçadores!</h1>",
                unsafe_allow_html=True)

    st.divider()
    st.text("""Sobre nós:
             
        A Associação dos Caçadores é a entidade que supervisiona e coordena todas as Guildas e Caçadores do país.
        Como a autoridade central responsável pela gestão e regulamentação das atividades dos caçadores,
        nossa corporação desempenha um papel vital na manutenção da ordem e na promoção da cooperação entre as guildas.""")
    st.divider()
    st.text("""Missão:

        Nossa missão é garantir que as guildas de caçadores operem de maneira eficaz e ética, promovendo os mais altos padrões de profissionalismo,
        integridade e excelência em todas as suas atividades. Estamos comprometidos em proteger os interesses dos caçadores e dos cidadãos,
        garantindo que as dungeons sejam exploradas de forma responsável e que as ameaças aos nossos mundos sejam enfrentadas com determinação e habilidade.""")
    st.divider()
    st.text("""Serviços:

        - Supervisão e regulamentação das atividades das guildas de caçadores.
        - Fornecimento de diretrizes e recursos para treinamento e desenvolvimento de caçadores.
        - Cooperação com autoridades locais e internacionais para garantir a segurança das fronteiras.
        - Investigação de incidentes e relatórios de atividades suspeitas nas dungeons.
        - Promoção da cooperação e colaboração entre as guildas para enfrentar ameaças em larga escala.""")
    st.divider()
    st.text("""Junte-se a nós:

        Se você é Presidente de Guilda ou um Caçador individual em busca de orientação e apoio, ou inda que busca se juntar a uma comunidade maior
        de profissionais dedicados, a Associação dos Caçadores está aqui para ajudar. Juntos, podemos enfrentar os desafios das dungeons, proteger nosso mundo
        e descobrir os segredos perdidos que aguardam além dos portais. Junte-se a nós e seja parte de uma tradição de excelência e coragem.""")
    st.divider()

    if st.button('Guildas Associadas'):
        guildas.guildas()
