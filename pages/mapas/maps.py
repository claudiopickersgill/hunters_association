import streamlit as st
import pandas as pd
from streamlit_folium import st_folium
import folium
from shapely.geometry import Point, Polygon


def maps():
    st.title("Portais Ativos nos Estados Unidos da América")
    st.write("Acompanhe aqui em tempo real os portais que estão ativos no país!")
    # st.write("Em breve!")
    st.divider()

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

    # # Função para adicionar marcadores ao mapa
    # def add_markers_to_map(m, points):
    #     for lat, lon in points:
    #         folium.Marker(location=[lat, lon],
    #                       icon=folium.Icon(color='red')).add_to(m)

    def add_markers_to_map(m, lat, long):
        folium.Marker(location=[lat, long],
                      icon=folium.Icon(color='red')).add_to(m)

    # # Função para verificar se um ponto está dentro do polígono
    # def check_location_in_us(location):
    #     point = Point(location["coords"])
    #     return us_polygon.contains(point)

    # Crie um mapa Folium
    m = folium.Map(location=initial_location, zoom_start=4)

    # Lendo os arquivos CSV e criando os polígonos
    file_paths = ['data/csv/ALASKA_CSV.csv',
                  'data/csv/BASE_CUBA_CSV.csv',
                  'data/csv/EUA_PONTOS_CSV.csv',
                  'data/csv/ILHA_OCEANO_CSV.csv']

    colors = ['blue', 'green', 'red', 'purple']
    polygons = []
    all_portals = []

    # portals_paths = ['data/csv/eua_portals.csv',
    #                  'data/csv/alaska_portals.csv',
    #                  'data/csv/cuba_portals.csv']

    portals = read_csv_to_points('data/csv/eua_portals.csv')

    # for portal_path in portals_paths:
    #     points = read_csv_to_points(portal_path)
    #     all_portals.append(points)

    for file_path in file_paths:
        points = read_csv_to_points(file_path)
        polygon = create_polygon(points)
        polygons.append(polygon)
        # all_portals.append(portals)

    for i, polygon in enumerate(polygons):
        # add_polygon_to_map(m, polygon, color=colors[i])

        def check_location_in_us(lat, lon):
            point = Point(lon, lat)  # Shapely usa (lon, lat)
            return polygon.contains(point)

        for lat, long in portals:
            if check_location_in_us(long, lat):
                add_markers_to_map(m, lat, long)
            else:
                pass

    # # Cria um polígono usando Shapely
    # us_polygon = Polygon(us_polygon_coords)

    # locations = [
    #     {"name": "São Francisco", "coords": (-122.4194, 37.7749)},
    #     {"name": "Los Angeles", "coords": (-118.2437, 34.0522)},
    #     {"name": "Nova York", "coords": (-74.0060, 40.7128)},
    #     {"name": "Chicago", "coords": (-87.6298, 41.8781)},
    #     {"name": "Toronto", "coords": (-79.3832, 43.6532)}  # Fora dos EUA
    # ]

    # Adicionar o polígono dos EUA ao mapa
    # folium.Polygon(locations=us_polygon_coords, color="grey",
    #                fill_opacity=0.1,
    #                weight=1,
    #                fill=False).add_to(m)

    # for location in locations:
    #     folium.Marker(
    #         # Invertendo para folium (lat, lon)
    #         location=location["coords"][::-1],
    #         popup=f"{location['name']} - Dentro dos EUA: {check_location_in_us(location)}",
    #         icon=folium.Icon(
    #             color="green" if check_location_in_us(location) else "red")
    #     ).add_to(m)

    # # Adicione um marcador ao mapa
    # folium.Marker(
    #     location=initial_location,
    #     popup="São Francisco",
    #     icon=folium.Icon(icon="cloud"),
    # ).add_to(m)

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
    st_folium(m, width=700, height=500)

    return
