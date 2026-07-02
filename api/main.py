from fastapi import FastAPI, Header, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from app.core.analyzer import DynamiCore

app = FastAPI(
    title="DynamiCore Ultra Luxe",
    version="4.0"
)

# =========================
# REQUEST MODEL
# =========================
class SystemRequest(BaseModel):
    system: list[int]


# =========================
# 💎 PREMIUM DASHBOARD (NO STREAMLIT)
# =========================
@app.get("/", response_class=HTMLResponse)
def dashboard():
    return """
<!DOCTYPE html>
<html>
<head>
<title>DynamiCore Ultra Luxe</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

<style>
body {
    margin:0;
    font-family: Arial;
    background: linear-gradient(135deg,#0b1020,#0f172a,#020617);
    color:white;
    text-align:center;
    padding:10px;
}

h1 {
    font-size:22px;
    background: linear-gradient(to right,#60a5fa,#a78bfa,#34d399);
    -webkit-background-clip: text;
    color: transparent;
}

.card {
    margin:12px;
    padding:16px;
    background: rgba(255,255,255,0.05);
    border-radius:16px;
    backdrop-filter: blur(10px);
    box-shadow: 0 0 20px rgba(0,0,0,0.4);
}

input {
    width:90%;
    padding:12px;
    border-radius:10px;
    border:none;
    font-size:14px;
}

button {
    margin-top:10px;
    padding:12px;
    width:90%;
    border-radius:10px;
    border:none;
    background:#22c55e;
    font-weight:bold;
    font-size:15px;
}

p {
    margin:6px;
    font-size:14px;
}
</style>
</head>

<body>

<h1>🧠 DynamiCore ULTRA LUXE</h1>

<div class="card">
    <input id="system" value="0,1,2,3,4,5">
    <button onclick="run()">ANALYZE SYSTEM</button>
</div>

<div class="card">
    <h3>METRICS</h3>
    <p id="entropy">Entropy: -</p>
    <p id="coherence">Coherence: -</p>
    <p id="chaos">Chaos: -</p>
    <p id="phase">Phase: -</p>
</div>

<div class="card">
    <h3>BASINS MAP</h3>
    <canvas id="chart"></canvas>
</div>

<script>

async function run() {
    try {
        const system = document.getElementById("system").value
            .split(",")
            .map(x => parseInt(x));

        const res = await fetch("/analyze", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "x-api-key": "dev"
            },
            body: JSON.stringify({ system })
        });

        const data = await res.json();

        if (!data.payload) {
            alert("Error: backend no devolvió payload");
            return;
        }

        const p = data.payload;

        document.getElementById("entropy").innerText =
            "Entropy: " + p.entropy;

        document.getElementById("coherence").innerText =
            "Coherence: " + p.coherence;

        document.getElementById("chaos").innerText =
            "Chaos: " + p.chaos;

        document.getElementById("phase").innerText =
            "Phase: " + p.phase;

        const labels = Object.keys(p.basins || {});
        const values = Object.values(p.basins || {});

        new Chart(document.getElementById("chart"), {
            type: "bar",
            data: {
                labels: labels,
                datasets: [{
                    label: "Basins Energy",
                    data: values,
                    backgroundColor: "#60a5fa"
                }]
            }
        });

    } catch (err) {
        alert("Error en análisis: " + err.message);
        console.log(err);
    }
}

</script>

</body>
</html>
"""


# =========================
# 🚀 API ENDPOINT
# =========================
@app.post("/analyze")
def analyze(req: SystemRequest, x_api_key: str = Header(...)):

    engine = DynamiCore(req.system)
    result = engine.analyze()

    if not isinstance(result, dict):
        raise HTTPException(status_code=500, detail="Invalid analysis output")

    return {
        "status": "ok",
        "payload": result
    }
