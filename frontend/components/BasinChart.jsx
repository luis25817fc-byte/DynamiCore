import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    BarElement,
    Tooltip,
    Legend
} from "chart.js";

import { Bar } from "react-chartjs-2";

ChartJS.register(
    CategoryScale,
    LinearScale,
    BarElement,
    Tooltip,
    Legend
);

export default function BasinChart({ basins }) {

    const labels = Object.keys(basins || {});

    const values = Object.values(basins || {});

    const data = {

        labels,

        datasets: [

            {

                label: "Dynamic Basins",

                data: values,

                backgroundColor: [

                    "#FFD700",

                    "#E6C200",

                    "#C9A227",

                    "#B8860B",

                    "#FFF4B2",

                    "#FFD700"

                ],

                borderColor: "#ffffff",

                borderWidth: 2,

                borderRadius: 8

            }

        ]

    };

    const options = {

        responsive: true,

        maintainAspectRatio: false,

        plugins: {

            legend: {

                labels: {

                    color: "#ffffff"

                }

            }

        },

        scales: {

            x: {

                ticks: {

                    color: "#ffffff"

                },

                grid: {

                    color: "rgba(255,255,255,0.05)"

                }

            },

            y: {

                beginAtZero: true,

                ticks: {

                    color: "#ffffff"

                },

                grid: {

                    color: "rgba(255,255,255,0.05)"

                }

            }

        }

    };

    return (

        <div
            style={{
                width: "100%",
                height: "450px"
            }}
        >

            <Bar
                data={data}
                options={options}
            />

        </div>

    );

              }
