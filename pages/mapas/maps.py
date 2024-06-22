import streamlit as st
import pandas as pd
from streamlit_folium import st_folium, folium_static
import folium
from shapely.geometry import Point, Polygon
import json
import utils_config
import random


def maps():
    st.title("Portais Ativos nos Estados Unidos da América")
    st.write("Acompanhe aqui em tempo real os portais que estão ativos no país!")
    # st.write("Em breve!")
    st.divider()

    config_file = "./config.json"
    config = utils_config.load_config(config_file)

    # Defina a localização inicial do mapa (latitude e longitude)
    initial_location = [39.976177, -97.728974]

    def read_csv_to_points(file_path):
        df = pd.read_csv(file_path)
        return [(row['y'], row['x']) for index, row in df.iterrows()]

    # Função para criar um polígono a partir de pontos
    def create_polygon(points):
        return Polygon(points)

    # Função para adicionar um polígono ao mapa
    def add_polygon_to_map(m, polygon, color='blue'):
        folium.Polygon(locations=[(lat, lon) for lat, lon in polygon.exterior.coords],
                       color=color, fill=True, fill_opacity=0.4).add_to(m)

    def add_markers_to_map(m, lat, long, rank, dias, prioridade):
        if prioridade == "alta":
            html = f"""Rank: {rank}<br>
                       Dias Abertos: {dias}<br>
                       Prioridade: {prioridade}"""
            iframe = folium.IFrame(html=html, width=150, height=80)
            popup = folium.Popup(iframe, max_width=300)
            folium.Marker(location=[long, lat],
                          popup=popup,
                          icon=folium.Icon(color='red')).add_to(m)
        elif prioridade == "media":
            html = f"""Rank: {rank}<br>
                       Dias Abertos: {dias}<br>
                       Prioridade: {prioridade}"""
            iframe = folium.IFrame(html=html, width=150, height=80)
            popup = folium.Popup(iframe, max_width=300)
            folium.Marker(location=[long, lat],
                          popup=popup,
                          icon=folium.Icon(color='darkgreen')).add_to(m)
        else:
            html = f"""Rank: {rank}<br>
                       Dias Abertos: {dias}<br>
                       Prioridade: {prioridade}"""
            iframe = folium.IFrame(html=html, width=150, height=80)
            popup = folium.Popup(iframe, max_width=300)
            folium.Marker(location=[long, lat],
                          popup=popup,
                          icon=folium.Icon(color='lightgreen')).add_to(m)

    def add_locals_to_map(m, config):
        for i in config:
            if i.name == "Guilda Sombras":
                pass
            elif i.name == "Quebra de Portal":
                html = f"""Nome: {i.name}<br>
                          Rank: {i.rank}<br>
                          Sede: {i.sede}"""
                iframe = folium.IFrame(html=html, width=300, height=80)
                popup = folium.Popup(iframe, max_width=300)
                folium.Marker(location=[i.lat, i.long],
                              popup=popup,
                              icon=folium.Icon(color="black")).add_to(m)
            else:
                html = f"""Nome: {i.name}<br>
                          Rank: {i.rank}<br>
                          Sede: {i.sede}"""
                iframe = folium.IFrame(html=html, width=300, height=80)
                popup = folium.Popup(iframe, max_width=300)
                folium.Marker(location=[i.lat, i.long],
                              popup=popup,
                              icon=folium.Icon(color="blue")).add_to(m)

    # # Função para verificar se um ponto está dentro do polígono
    # def check_location_in_us(location):
    #     point = Point(location["coords"])
    #     return us_polygon.contains(point)

    # Crie um mapa Folium
    m = folium.Map(location=initial_location, zoom_start=4)

    # Lendo os arquivos CSV e criando os polígonos
    # file_paths = ['data/csv/ALASKA_CSV.csv',
    #                 'data/csv/EUA_PONTOS_CSV.csv']
    # colors = ['blue', 'green', 'red', 'purple']
    # polygons = []
    # all_portals = []

    # portals = read_csv_to_points('data/csv/portals.csv')
    portals_df = pd.DataFrame(pd.read_csv('data/csv/portals.csv'))

    # for file_path in file_paths:
    #     points = read_csv_to_points(file_path)
    #     polygon = create_polygon(points)
    #     polygons.append(polygon)

    us_points = read_csv_to_points('data/csv/EUA_PONTOS_CSV.csv')
    alaska_points = read_csv_to_points('data/csv/ALASKA_CSV.csv')
    us_polygon = create_polygon(us_points)
    alaska_polygon = create_polygon(alaska_points)

    # for i, polygon in enumerate(polygons):
    # add_polygon_to_map(m, us_polygon, color="blue")
    # add_polygon_to_map(m, alaska_polygon, color="green")

    # def check_location_in_us(lat, lon):
    #     point = Point(lon, lat)  # Shapely usa (lon, lat)
    #     return polygon.contains(point)

    X = 250  # Altere este valor conforme necessário

    # Selecionar aleatoriamente X linhas do DataFrame
    random_indices = random.sample(range(len(portals_df)), X)
    random_rows = portals_df.iloc[random_indices]

    def plot_markers():
        for index, row in random_rows.iterrows():
            point = Point(row['y'], row['x'])
            if (us_polygon.contains(point) == True) or (alaska_polygon.contains(point) == True):
                add_markers_to_map(
                    m, row["x"], row["y"], row["rank"], row["dias_aberto"], row["prioridade"])

    plot_markers()
    add_locals_to_map(m, config)

    # Adicione a chave de API do Google Maps ao Folium (opcional)
    # Você pode adicionar camadas do Google Maps (se necessário)
    folium.TileLayer(
        tiles='https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',
        attr='Google',
        name='Google Satellite',
        overlay=True,
        control=True
    ).add_to(m)

    # Adicionar controles de camada
    folium.LayerControl().add_to(m)

    # Use st_folium para renderizar o mapa no Streamlit
    # st.title("Mapa Interativo com Google Maps e Streamlit")
    folium_static(m, width=700, height=500)

    return
