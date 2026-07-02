from fastapi import FastAPI, Header, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import uuid

from app.core.analyzer import DynamiCore
from app.core.db import init_db, create_user, get_user, upgrade_user, increment
from app.core.auth import validate_user
from app.core.stripe_service import checkout
from app.core.security import create_token

app = FastAPI(title="DynamiCore Silicon Valley SaaS")

init_db()


class Req(BaseModel):
    system: list[int]


# =========================
# FRONTEND SAAS UI
# =========================
@app.get("/", response_class=HTMLResponse)
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<style>
body { background:#0a0f1c; color:white; font-family:Arial; text-align:center; }
.card { background:#111827; margin:10px; padding:10px; border-radius:10px; }
button { width:90%; padding:10px; background:#d4af37; border:none; }
input { width:90%; padding:10px; }
</style>
</head>

<body>

<h2>🧠 DynamiCore Silicon Valley SaaS</h2>

<div class="card">
<input id="system" value="0,1,2,3,4,5">
<button onclick="run()">Analyze</button>
</div>

<div class="card">
<p id="e">Entropy -</p>
<p id="c">Coherence -</p>
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
"x-api-key":"demo"
},
body: JSON.stringify({system})
});

const data = await res.json();

const p = data.payload;

document.getElementById("e").innerText = p.entropy;
document.getElementById("c").innerText = p.coherence;

const labels = Object.keys(p.basins);
const values = Object.values(p.basins);

if(chart) chart.destroy();

chart = new Chart(document.getElementById("chart"), {
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
# ANALYZE API
# =========================
@app.post("/analyze")
def analyze(req: Req, x_api_key: str = Header(...)):

    user = validate_user(x_api_key)

    if not user:
        raise HTTPException(401, "Invalid API key")

    if user == "LIMIT":
        raise HTTPException(429, "Limit reached")

    engine = DynamiCore(req.system)
    result = engine.analyze()

    increment(x_api_key)

    return {"payload": result}


# =========================
# CREATE USER (REAL SIGNUP)
# =========================
@app.get("/signup")
def signup():

    api_key = str(uuid.uuid4())
    create_user(api_key)

    token = create_token(api_key)

    return {
        "api_key": api_key,
        "token": token
    }


# =========================
# STRIPE CHECKOUT
# =========================
@app.get("/upgrade/{api_key}")
def upgrade(api_key: str):

    url = checkout(api_key)

    return {"checkout_url": url}


# =========================
# STRIPE WEBHOOK (PRO UPGRADE)
# =========================
@app.post("/stripe/webhook")
async def stripe_webhook():

    # aquí Stripe te manda evento real
    # payment_success → upgrade_user(api_key)

    return {"status": "ok"}
