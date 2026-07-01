import streamlit as st
import requests
import pandas as pd

# =========================
# CONFIG
# =========================
API_URL = "https://dynamicore.onrender.com/analyze"
API_KEY = "dev-key-123"

st.set_page_config(page_title="DynamiCore Dashboard", layout="wide")

st.title("🧠 DynamiCore Dashboard")
st.subheader("Análisis de sistemas dinámicos")

# =========================
# INPUT
# =========================
system_input = st.text_input("Sistema (ej: 0,1,2,3,4,5)", "0,1,2,3,4,5")
system = [int(x) for x in system_input.split(",") if x.strip().isdigit()]

# =========================
# BOTÓN
# =========================
if st.button("🚀 Analizar"):

    with st.spinner("Procesando..."):

        try:
            response = requests.post(
                API_URL,
                headers={"x-api-key": API_KEY},
                json={"system": system}
            )

            st.write("Status:", response.status_code)

            if response.status_code != 200:
                st.error(response.text)
                st.stop()

            data = response.json()["payload"]

            # =========================
            # METRICAS
            # =========================
            col1, col2, col3 = st.columns(3)

            col1.metric("🔥 Entropía", data.get("entropy", 0))
            col2.metric("🧠 Coherencia", data.get("coherence", 0))
            col3.metric("⚙️ Tamaño", len(system))

            # =========================
            # CICLOS
            # =========================
            st.subheader("🔁 Ciclos")
            st.write(data.get("cycles", []))

            # =========================
            # BASINS
            # =========================
            st.subheader("📊 Basins")
            basins = data.get("basins", {})

            if basins:
                df = pd.DataFrame({
                    "Ciclo": list(basins.keys()),
                    "Tamaño": list(basins.values())
                })
                st.bar_chart(df.set_index("Ciclo"))

            # =========================
            # GRAFO
            # =========================
            st.subheader("🧠 Grafo")
            st.json(data.get("graph", {}))

            # =========================
            # RAW
            # =========================
            with st.expander("🔬 Raw JSON"):
                st.json(data)

        except Exception as e:
            st.error(f"Error: {e}")
