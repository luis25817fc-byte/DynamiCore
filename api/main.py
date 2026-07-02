from fastapi import FastAPI, Header, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from app.core.analyzer import DynamiCore
from app.core.auth import get_user_by_key, check_limit, increment_usage

app = FastAPI(title="DynamiCore API", version="2.0")


class SystemRequest(BaseModel):
    system: list[int]


# =========================
# FRONTEND
# =========================
@app.get("/", response_class=HTMLResponse)
def dashboard():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>DynamiCore</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

    <style>
        body {
            font-family: Arial;
            background: #0f172a;
            color: white;
            text-align: center;
        }

        input, button {
            padding: 10px;
            margin: 5px;
        }

        .card {
            background: #1e293b;
            padding: 20px;
            margin: 20px;
            border-radius: 10px;
        }
    </style>
</head>

<body>

<h1>🧠 DynamiCore Dashboard</h1>

<div class="card">
    <input id="system" value="0,1,2,3,4,5" style="width:300px;">
    <br>
    <button onclick="runAnalysis()">Analizar</button>
</div>

<div class="card">
    <h3>Resultados</h3>
    <p id="entropy">Entropía: -</p>
    <p id="coherence">Coherencia: -</p>
</div>

<div class="card">
    <h3>Basins</h3>
    <canvas id="chart"></canvas>
</div>

<script>
let chartInstance = null;

async function runAnalysis() {

    try {
        const system = document.getElementById("system").value
            .split(",")
            .map(x => parseInt(x));

        const res = await fetch("/analyze", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "x-api-key": "dev-key-123"
            },
            body: JSON.stringify({ system })
        });

        const data = await res.json();

        if (!data || !data.payload) {
            throw new Error("Respuesta vacía del servidor");
        }

        const payload = data.payload;

        // ======================
        // MÉTRICAS
        // ======================
        document.getElementById("entropy").innerText =
            "Entropía: " + payload.entropy;

        document.getElementById("coherence").innerText =
            "Coherencia: " + payload.coherence;

        // ======================
        // BASINS
        // ======================
        const labels = Object.keys(payload.basins);
        const values = Object.values(payload.basins);

        // destruir gráfico anterior
        if (chartInstance) chartInstance.destroy();

        chartInstance = new Chart(
            document.getElementById("chart"),
            {
                type: "bar",
                data: {
                    labels: labels,
                    datasets: [{
                        label: "Basins",
                        data: values,
                        backgroundColor: "#d4af37",
                        borderColor: "#ffffff",
                        borderWidth: 2
                    }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: {
                            labels: { color: "#ffffff" }
                        }
                    },
                    scales: {
                        x: {
                            ticks: { color: "#ffffff" }
                        },
                        y: {
                            ticks: { color: "#a0a0a0" },
                            beginAtZero: true
                        }
                    }
                }
            }
        );

    } catch (err) {
        alert("Error en análisis: " + err.message);
    }
}
</script>

</body>
</html>
    """


# =========================
# API
# =========================
@app.post("/analyze")
def analyze(req: SystemRequest, x_api_key: str = Header(..., alias="x-api-key")):

    user, data = get_user_by_key(x_api_key)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    if not check_limit(data):
        raise HTTPException(status_code=429, detail="Limit reached")

    engine = DynamiCore(req.system)
    result = engine.analyze()

    increment_usage(user)

    return {
        "status": "success",
        "user": user,
        "plan": data["plan"],
        "payload": result
    }
