from fastapi import FastAPI, Header
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from app.core.analyzer import DynamiCore
from app.core.auth import get_user_by_key, check_limit, increment_usage

app = FastAPI(title="DynamiCore API", version="2.0")


# =========================
# REQUEST MODEL
# =========================
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
                margin: 10px;
                border-radius: 8px;
                border: none;
            }

            button {
                background: #2563eb;
                color: white;
                cursor: pointer;
            }

            .card {
                background: #1e293b;
                margin: 20px;
                padding: 20px;
                border-radius: 12px;
            }

            #error {
                color: red;
            }
        </style>
    </head>

    <body>

        <h1>🧠 DynamiCore Dashboard</h1>

        <div class="card">
            <input id="system" value="0,1,2,3,4,5" style="width:300px;">
            <br>
            <button onclick="run()">Analizar</button>
        </div>

        <div class="card">
            <h3>Resultados</h3>
            <p id="entropy">Entropía: -</p>
            <p id="coherence">Coherencia: -</p>
            <p id="error"></p>
        </div>

        <div class="card">
            <h3>Basins</h3>
            <canvas id="chart"></canvas>
        </div>

        <script>
        async function run() {
            try {
                document.getElementById("error").innerText = "";

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

                console.log(data); // debug real

                if (data.status !== "success" || !data.payload) {
                    document.getElementById("error").innerText =
                        data.message || "Error desconocido del backend";
                    return;
                }

                const payload = data.payload;

                document.getElementById("entropy").innerText =
                    "Entropía: " + (payload.entropy ?? "N/A");

                document.getElementById("coherence").innerText =
                    "Coherencia: " + (payload.coherence ?? "N/A");

                const basins = payload.basins || {};

                const labels = Object.keys(basins);
                const values = Object.values(basins);

                if (window.myChart) window.myChart.destroy();

                window.myChart = new Chart(
                    document.getElementById("chart"),
                    {
                        type: "bar",
                        data: {
                            labels: labels,
                            datasets: [{
                                label: "Basins",
                                data: values
                            }]
                        }
                    }
                );

            } catch (err) {
                document.getElementById("error").innerText =
                    "Error: " + err.message;
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
def analyze(
    req: SystemRequest,
    x_api_key: str = Header(..., alias="x-api-key")
):

    try:
        user, data = get_user_by_key(x_api_key)

        if not user:
            return {"status": "error", "message": "Invalid API Key"}

        if not check_limit(data):
            return {"status": "error", "message": "Limit reached"}

        engine = DynamiCore(req.system)
        result = engine.analyze()

        increment_usage(user)

        return {
            "status": "success",
            "payload": result
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }
