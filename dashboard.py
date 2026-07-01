import streamlit as st
import requests
import matplotlib.pyplot as plt

# =========================
# CONFIG
# =========================
API_URL = "https://dynamicore.onrender.com/analyze"
API_KEY = "dev-key-123"

st.set_page_config(
    page_title="DynamiCore Dashboard",
    layout="centered"
)

st.title("🧠 DynamiCore Visual Dashboard")
st.subheader("Análisis de sistemas dinámicos")

# =========================
# INPUT DEL USUARIO
# =========================
system_input = st.text_input(
    "Ingresa sistema (ej: 1,2,0,4,5,3)",
    "1,2,0,4,5,3"
)

# =========================
# BOTÓN
# =========================
if st.button("Analizar sistema"):
    
    system = [int(x.strip()) for x in system_input.split(",")]

    payload = {
        "system": system
    }

    headers = {
        "x-api-key": API_KEY,
        "Content-Type": "application/json"
    }

    # =========================
    # LLAMADA A TU API (RENDER)
    # =========================
    response = requests.post(API_URL, json=payload, headers=headers)

    if response.status_code == 200:
        data = response.json()["payload"]

        st.success("Análisis completado")

        # =========================
        # RESULTADOS NUMÉRICOS
        # =========================
        st.write("### 📊 Resultados")
        st.json(data)

        # =========================
        # ENTROPÍA Y COHERENCIA
        # =========================
        col1, col2 = st.columns(2)

        col1.metric("Entropy", round(data["entropy"], 4))
        col2.metric("Coherence", round(data["coherence"], 4))

        # =========================
        # GRAFICO SIMPLE DE BASINS
        # =========================
        st.write("### 🧩 Cuencas de Atracción")

        basins = data["basins"]

        labels = list(basins.keys())
        values = list(basins.values())

        fig, ax = plt.subplots()
        ax.bar(labels, values)
        ax.set_title("Basins Distribution")

        st.pyplot(fig)

        # =========================
        # CICLOS
        # =========================
        st.write("### 🔁 Ciclos detectados")
        st.write(data["cycles"])

    else:
        st.error("Error al conectar con la API")
