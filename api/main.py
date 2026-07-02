from fastapi import FastAPI, Header, HTTPException
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
# FRONTEND (HTML + JS)
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
                margin: 0;
                padding: 0;
            }

            input, button {
                padding: 10px;
                margin: 8px;
                border-radius: 8px;
                border: none;
            }

            button {
                cursor: pointer;
                background: #2563eb;
                color: white;
            }

            .card {
                background: #1e293b;
                padding: 20px;
                margin: 20px;
                border-radius: 12px;
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

                const text = await res.text();

                const data = JSON.parse(text);

                const payload = data.payload;

                document.getElementById("entropy").innerText =
                    "Entropía: " + payload.entropy;

                document.getElementById("coherence").innerText =
                    "Coherencia: " + payload.coherence;

                const labels = Object.keys(payload.basins);
                const values = Object.values(payload.basins);

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
            }
        }
        </script>

    </body>
    </html>
    """


# =========================
# API ENDPOINT
# =========================
@app.post("/analyze")
def analyze(
    req: SystemRequest,
    x_api_key: str = Header(..., alias="x-api-key")
):

    # auth
    user, data = get_user_by_key(x_api_key)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    if not check_limit(data):
        raise HTTPException(status_code=429, detail="Limit reached")

    try:
        engine = DynamiCore(req.system)
        result = engine.analyze()

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    increment_usage(user)

    return {
        "status": "success",
        "user": user,
        "plan": data["plan"],
        "payload": result
    }
