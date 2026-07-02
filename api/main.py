from fastapi import FastAPI, Header, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from app.core.analyzer import DynamiCore

app = FastAPI(title="DynamiCore API", version="3.0")


class SystemRequest(BaseModel):
    system: list[int]


# =========================
# FRONTEND (CELULAR FRIENDLY)
# =========================
@app.get("/", response_class=HTMLResponse)
def dashboard():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>DynamiCore PRO</title>
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

        <style>
            body {
                font-family: Arial;
                background: #0f172a;
                color: white;
                text-align: center;
                padding: 10px;
            }

            input, button {
                padding: 12px;
                margin: 6px;
                width: 90%;
                border-radius: 8px;
            }

            button {
                background: #22c55e;
                color: black;
                font-weight: bold;
            }

            .card {
                background: #1e293b;
                padding: 15px;
                margin: 15px;
                border-radius: 12px;
            }
        </style>
    </head>

    <body>
        <h2>🧠 DynamiCore PRO</h2>

        <div class="card">
            <input id="system" value="0,1,2,3,4,5" />
            <button onclick="run()">Analizar</button>
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
        async function run() {
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

                if (!data.payload) {
                    alert("Error: backend no devolvió payload");
                    return;
                }

                const payload = data.payload;

                document.getElementById("entropy").innerText =
                    "Entropía: " + payload.entropy.toFixed(6);

                document.getElementById("coherence").innerText =
                    "Coherencia: " + payload.coherence.toFixed(6);

                const labels = Object.keys(payload.basins || {});
                const values = Object.values(payload.basins || {});

                new Chart(document.getElementById("chart"), {
                    type: "bar",
                    data: {
                        labels: labels,
                        datasets: [{
                            label: "Basins",
                            data: values
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
# API CORE
# =========================
@app.post("/analyze")
def analyze(req: SystemRequest, x_api_key: str = Header(..., alias="x-api-key")):

    engine = DynamiCore(req.system)
    result = engine.analyze()

    if not isinstance(result, dict):
        raise HTTPException(status_code=500, detail="Invalid analyzer output")

    return {
        "status": "success",
        "payload": result
    }
