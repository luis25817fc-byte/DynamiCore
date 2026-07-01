import streamlit as st
import requests
import pandas as pd

# =========================
# CONFIG
# =========================
API_URL = "https://dynamicore.onrender.com/analyze"

# 🔐 IMPORTANTE: luego esto lo pasamos a secrets
API_KEY = "dev-key-123"

st.set_page_config(
    page_title="DynamiCore Dashboard",
    layout="wide"
)

st.title("🧠 DynamiCore Dashboard")
st.caption("Sistema de análisis dinámico en producción")

# =========================
# INPUT
# =========================
st.sidebar.header("⚙️ Configuración")

system_input = st.sidebar.text_input(
    "Sistema dinámico (ej: 0,1,2,3,4,5)",
    "0,1,2,3,4,5"
)

system = [
    int(x.strip())
    for x in system_input.split(",")
    if x.strip().isdigit()
]

run = st.sidebar.button("🚀 Analizar")


# =========================
# RUN
# =========================
if run:

    with st.spinner("Ejecutando DynamiCore... 🧠"):

        try:
            response = requests.post(
                API_URL,
                headers={"x-api-key": API_KEY},
                json={"system": system},
                timeout=30
            )

            st.write("Status:", response.status_code)

            if response.status_code != 200:
                st.error(response.text)
                st.stop()

            data = response.json()["payload"]

            # =========================
            # MÉTRICAS
            # =========================
            st.markdown("## 📊 Métricas")

            c1, c2, c3 = st.columns(3)

            c1.metric("🔥 Entropía", f"{data.get('entropy', 0):.4f}")
            c2.metric("🧠 Coherencia", f"{data.get('coherence', 0):.2f}")
            c3.metric("⚙️ Estados", len(system))

            # =========================
            # CICLOS
            # =========================
            st.markdown("## 🔁 Ciclos")

            cycles = data.get("cycles", [])
            st.dataframe(pd.DataFrame({"Ciclos": [str(c) for c in cycles]}))

            # =========================
            # BASINS
            # =========================
            st.markdown("## 📊 Basins")

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
            st.markdown("## 🧠 Grafo")

            graph = data.get("graph", {})

            if isinstance(graph, dict):
                st.write("Nodos:", graph.get("nodes", []))
                st.dataframe(graph.get("edges", []))
            else:
                st.json(graph)

            # =========================
            # DEBUG
            # =========================
            with st.expander("🔬 Raw JSON"):
                st.json(data)

        except Exception as e:
            st.error(f"Error: {str(e)}")
