from fastapi import FastAPI, Header, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from app.core.analyzer import DynamiCore
from app.core.db import init_db, create_user
from app.core.auth import validate_key

app = FastAPI(title="DynamiCore SaaS", version="1.0")


# =========================
# INIT DB
# =========================
init_db()


# =========================
# REQUEST
# =========================
class RequestModel(BaseModel):
    system: list[int]


# =========================
# FRONTEND
# =========================
@app.get("/", response_class=HTMLResponse)
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<style>
body { background:#0b0f19; color:white; text-align:center; font-family:Arial; }
.card { margin:10px; padding:10px; background:#111827; border-radius:10px; }
button { padding:10px; background:#d4af37; border:none; width:90%; }
input { width:90%; padding:10px; }
</style>
</head>

<body>

<h2>🧠 DynamiCore SaaS</h2>

<div class="card">
<input id="system" value="0,1,2,3,4,5">
<button onclick="run()">Analizar</button>
</div>

<div class="card">
<p id="e">Entropía: -</p>
<p id="c">Coherencia: -</p>
</div>

<div class="card">
<canvas id="chart"></canvas>
</div>

<script>

let chart;

async function run(){

const system = document.getElementById("system")
.value.split(",")
.map(x => parseInt(x));

const res = await fetch("/analyze", {
method:"POST",
headers:{
"Content-Type":"application/json",
"x-api-key":"demo-key"
},
body: JSON.stringify({system})
});

const data = await res.json();

if(!data.payload){
alert("error");
return;
}

const p = data.payload;

document.getElementById("e").innerText = "Entropía: " + p.entropy;
document.getElementById("c").innerText = "Coherencia: " + p.coherence;

const labels = Object.keys(p.basins);
const values = Object.values(p.basins);

if(chart) chart.destroy();

chart = new Chart(document.getElementById("chart"),{
type:"bar",
data:{
labels,
datasets:[{
label:"Basins",
data:values,
backgroundColor:"#d4af37"
}]
}
});

}

</script>

</body>
</html>
"""


# =========================
# ANALYZE ENDPOINT
# =========================
@app.post("/analyze")
def analyze(req: RequestModel, x_api_key: str = Header(...)):

    user = validate_key(x_api_key)

    if user is None:
        raise HTTPException(401, "Invalid API Key")

    if user == "LIMIT":
        raise HTTPException(429, "Limit reached")

    engine = DynamiCore(req.system)
    result = engine.analyze()

    return {
        "status": "ok",
        "payload": result
    }
