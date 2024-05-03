import streamlit as st
import pandas as pd
from pages.conexao import cria_df
# import matplotlib.pyplot as plt
# import seaborn as sns
# import numpy as np


def visual(user_name, user_type):
    if user_type == "hunter":
        df_hunters, _ = cria_df.cria_df()
        df_hunters.drop(["login", "senha"], axis=1, inplace=True)
        st.write(df_hunters[df_hunters['nome'] == user_name])
    else:
        _, df_guildas = cria_df.cria_df()
        df_guildas.drop(["login", "senha"], axis=1, inplace=True)
        st.write(df_guildas[df_guildas['nome_guida'] == user_name])
    st.divider()
