
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.set_page_config(layout="wide")
st.title("Deteksi Dini Titik Api - Kalimantan Timur")

url = "https://firms.modaps.eosdis.nasa.gov/data/active_fire/viirs_csv/VIIRS_I_Global_24h.csv"
df = pd.read_csv(url)

# Filter Kalimantan Timur
df = df[(df['latitude'] >= -2.0) & (df['latitude'] <= 3.0)]
df = df[(df['longitude'] >= 115.0) & (df['longitude'] <= 120.0)]

m = folium.Map(location=[0.5, 117.0], zoom_start=6)
for _, row in df.iterrows():
    folium.CircleMarker(
        location=[row['latitude'], row['longitude']],
        radius=4,
        color='red',
        fill=True,
        fill_opacity=0.7,
        popup=f"Tanggal: {row['acq_date']}, Satelit: {row['satellite']}"
    ).add_to(m)

st.subheader(f"Titik api ditemukan: {len(df)}")
st_data = st_folium(m, width=800)
