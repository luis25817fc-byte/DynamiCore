import streamlit as st
import requests
import matplotlib.pyplot as plt
import numpy as np

# =========================
# CONFIG
# =========================
API_URL = "https://dynamicore.onrender.com/analyze"

st.set_page_config(
    page_title="DynamiCore Pro",
    layout="wide"
)

# =========================
# UI HEADER
# =========================
st.title("🧠 DynamiCore Pro Dashboard")
st.caption("Sistema de análisis de dinámica discreta")

# =========================
# SIDEBAR (ESTILO SaaS)
# =========================
st.sidebar.title("Configuración")

api_key = st.sidebar.text_input("API Key", type="password", value="dev-key-123")

system_input = st.sidebar.text_input(
    "Sistema",
    "1,2,0,4,5,3"
)

run = st.sidebar.button("▶ Ejecutar análisis")

# =========================
# MAIN
# =========================
if run:

    system = [int(x.strip()) for x in system_input.split(",")]

    payload = {"system": system}

    headers = {
        "x-api-key": api_key,
        "Content-Type": "application/json"
    }

    response = requests.post(API_URL, json=payload, headers=headers)

    if response.status_code == 200:

        data = response.json()["payload"]

        # =========================
        # KPIs
        # =========================
        col1, col2, col3 = st.columns(3)

        col1.metric("Entropy", round(data["entropy"], 4))
        col2.metric("Coherence", round(data["coherence"], 4))
        col3.metric("Cycles", len(data["cycles"]))

        st.divider()

        # =========================
        # BASINS (VISUAL PRO)
        # =========================
        st.subheader("🧩 Basins of Attraction")

        basins = data["basins"]

        labels = list(basins.keys())
        values = list(basins.values())

        fig, ax = plt.subplots()

        ax.barh(labels, values, color="#4CAF50")
        ax.set_xlabel("Size")
        ax.set_title("Attractor Basins")

        st.pyplot(fig)

        # =========================
        # CYCLES VISUAL
        # =========================
        st.subheader("🔁 Cycles Structure")

        cycles = data["cycles"]

        fig2, ax2 = plt.subplots()

        for i, cycle in enumerate(cycles):
            x = np.arange(len(cycle))
            y = cycle
            ax2.plot(x, y, marker="o", label=f"Cycle {i}")

        ax2.set_title("Cycle Dynamics")
        ax2.legend()

        st.pyplot(fig2)

        # =========================
        # RAW DATA (DEBUG PRO)
        # =========================
        with st.expander("📦 Raw Data"):
            st.json(data)

    else:
        st.error("Error llamando API. Revisa API Key o backend.")
