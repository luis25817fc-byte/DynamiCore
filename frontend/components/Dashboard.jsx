import { useEffect, useState } from "react";

import api from "../api";

import Navbar from "./Navbar";
import MetricsCard from "./MetricsCard";
import BasinChart from "./BasinChart";

export default function Dashboard() {

    const [system, setSystem] = useState("0,1,2,3,4,5");

    const [entropy, setEntropy] = useState("-");

    const [coherence, setCoherence] = useState("-");

    const [basins, setBasins] = useState({});

    const [loading, setLoading] = useState(false);

    const [error, setError] = useState("");

    async function analyze() {

        setLoading(true);

        setError("");

        try {

            const response = await api.post(
                "/analyze",
                {
                    system: system
                        .split(",")
                        .map((n) => Number(n.trim()))
                },
                {
                    headers: {
                        "x-api-key": "dev-key-123"
                    }
                }
            );

            const payload = response.data.payload;

            setEntropy(Number(payload.entropy).toFixed(6));

            setCoherence(Number(payload.coherence).toFixed(6));

            setBasins(payload.basins);

        } catch (err) {

            console.error(err);

            setError("No fue posible analizar el sistema.");

        }

        setLoading(false);

    }

    useEffect(() => {

        analyze();

    }, []);

    return (

        <>

            <Navbar />

            <div className="container">

                <div className="hero">

                    <h1>DynamiCore PRO</h1>

                    <p>

                        Scientific Dynamic Intelligence Platform

                    </p>

                </div>

                <div className="inputCard">

                    <input

                        value={system}

                        onChange={(e) => setSystem(e.target.value)}

                    />

                    <button onClick={analyze}>

                        {loading ? "Analizando..." : "Analizar"}

                    </button>

                </div>

                {error !== "" && (

                    <div className="error">

                        {error}

                    </div>

                )}

                <div className="metricsGrid">

                    <MetricsCard

                        title="Entropy"

                        value={entropy}

                    />

                    <MetricsCard

                        title="Coherence"

                        value={coherence}

                    />

                </div>

                <div className="chartCard">

                    <BasinChart basins={basins} />

                </div>

            </div>

        </>

    );

                          }
