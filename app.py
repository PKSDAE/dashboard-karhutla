
import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(layout="wide")
st.title("📊 Sebaran Hotspot Kalimantan Timur (Data Sipongi)")

# Upload file Excel
uploaded_file = st.sidebar.file_uploader("Unggah file Excel dari Sipongi", type=["xls", "xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)

    st.subheader("📌 Tabel Data Hotspot")
    st.dataframe(df)

    st.subheader("📈 Grafik Jumlah Titik Api per Kabupaten/Kota")
    bar_chart = (
        alt.Chart(df)
        .mark_bar()
        .encode(
            x=alt.X("Kab Kota:N", sort='-y', title="Kabupaten/Kota"),
            y=alt.Y("Counter:Q", title="Jumlah Titik Api"),
            color=alt.Color("Satelit:N", title="Satelit"),
            tooltip=["Kab Kota", "Counter", "Satelit", "Confidence"]
        )
        .properties(width=800, height=400)
    )
    st.altair_chart(bar_chart)

    st.subheader("🔎 Filter")
    selected_satellite = st.selectbox("Pilih Satelit", options=["Semua"] + sorted(df["Satelit"].unique().tolist()))
    selected_confidence = st.selectbox("Pilih Confidence", options=["Semua"] + sorted(df["Confidence"].unique().tolist()))

    filtered_df = df.copy()
    if selected_satellite != "Semua":
        filtered_df = filtered_df[filtered_df["Satelit"] == selected_satellite]
    if selected_confidence != "Semua":
        filtered_df = filtered_df[filtered_df["Confidence"] == selected_confidence]

    st.write(f"Jumlah data setelah filter: {len(filtered_df)}")
    st.dataframe(filtered_df)

else:
    st.warning("Silakan upload file Excel dari Sipongi untuk melihat data.")
