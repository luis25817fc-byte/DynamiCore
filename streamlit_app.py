import streamlit as st
import requests
import pandas as pd

API_URL = "https://dynamicore.onrender.com/analyze"
API_KEY = "dev-key-123"

st.set_page_config(page_title="DynamiCore Dashboard", layout="wide")

st.title("🧠 DynamiCore Dashboard")

st.sidebar.header("⚙️ Configuración")

system_input = st.sidebar.text_input("Sistema", "0,1,2,3,4,5")

system = [int(x) for x in system_input.split(",") if x.strip().isdigit()]

if st.sidebar.button("🚀 Analizar"):

    st.write("Conectando a API...")

    try:
        r = requests.post(
            API_URL,
            headers={"x-api-key": API_KEY},
            json={"system": system},
            timeout=15
        )

        if r.status_code != 200:
            st.error(r.text)
            st.stop()

        data = r.json()["payload"]

        st.metric("Entropía", data["entropy"])
        st.metric("Coherencia", data["coherence"])

        st.write("Ciclos")
        st.json(data["cycles"])

        st.write("Basins")
        st.bar_chart(pd.DataFrame({
            "grupo": list(data["basins"].keys()),
            "valor": list(data["basins"].values())
        }).set_index("grupo"))

        st.write("Grafo")
        st.json(data["graph"])

    except Exception as e:
        st.error(str(e))
