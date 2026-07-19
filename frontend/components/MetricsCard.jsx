export default function MetricsCard({ title, value }) {

    return (

        <div className="metricCard">

            <div className="metricTitle">

                {title}

            </div>

            <div className="metricValue">

                {value}

            </div>

        </div>

    );

}
