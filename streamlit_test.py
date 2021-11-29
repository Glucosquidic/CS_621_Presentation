import streamlit as st
import folium
import pandas as pd
import json
from streamlit_folium import folium_static

st.set_page_config(layout = "wide")
st.title('Learning Streamlit')
jsonData = f"us-state-boundaries.geojson"




usMap = folium.Map(location = [39.8283, -98.5795], tiles = 'CartoDB positron', name = "Light Map",
                   zoom_start = 4, attr = "My Data attribution")


us_covid = pd.read_csv('states_covid.csv')

choice = ['riskLevels.icuCapacityRatio', 'metrics.icuCapacityRatio']

choice_selected = st.selectbox("Select choice", choice)


folium.Choropleth(
    geo_data = jsonData,
    name = "choropleth",
    data = us_covid,
    columns = ["state", choice_selected],
    key_on = "feature.properties.stusab",
    fill_color = "Oranges",
    fill_opacity = 0.7,
    line_opacity = 0.1,
    legend_name = choice_selected,
    highlight = True
).add_to(usMap)

folium.features.GeoJson('us-state-boundaries.geojson',
name = "States", popup = folium.features.GeoJsonPopup(fields = ["basename"])).add_to(usMap)

folium_static(usMap, width = 1600, height = 950)
