import streamlit as st
import pandas as pd
from pages.conexao import conexao


def cria_df():
    worksheet_hunters, worksheet_guilds = conexao.faz_conexao()
    dataframe_hunters = pd.DataFrame(worksheet_hunters.get_all_records())
    dataframe_guilds = pd.DataFrame(worksheet_guilds.get_all_records())

    return dataframe_hunters, dataframe_guilds
