
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.set_page_config(layout="wide")
st.title("🛰️ Dashboard Deteksi Dini Titik Api - Kalimantan Timur")

# Upload manual file CSV dari FIRMS
st.sidebar.header("📂 Upload Data Hotspot")
uploaded_file = st.sidebar.file_uploader("Unggah file CSV dari FIRMS (VIIRS/MODIS)", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # Filter wilayah Kalimantan Timur (perkiraan bounding box)
    df = df[(df['latitude'] >= -2.0) & (df['latitude'] <= 3.0)]
    df = df[(df['longitude'] >= 115.0) & (df['longitude'] <= 120.0)]

    # Peta
    m = folium.Map(location=[0.5, 117.0], zoom_start=6, tiles='cartodbpositron')

    for _, row in df.iterrows():
        color = 'red' if row.get('brightness', 300) > 330 else 'orange'
        popup_info = f"Tanggal: {row['acq_date']}<br>Satelit: {row['satellite']}<br>Brightness: {row.get('brightness', '-')}"
        folium.CircleMarker(
            location=[row['latitude'], row['longitude']],
            radius=4,
            color=color,
            fill=True,
            fill_opacity=0.7,
            popup=popup_info
        ).add_to(m)

    st.success(f"Titik api terdeteksi: {len(df)}")
    st_data = st_folium(m, width=900, height=500)

else:
    st.warning("Silakan upload file CSV dari FIRMS untuk melihat peta titik api.")
