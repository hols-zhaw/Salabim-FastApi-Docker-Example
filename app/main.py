from fastapi import FastAPI, Query
from typing import Optional
from simulation import simulate

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI in Docker!"}


@app.get("/api/v1/simulate")
async def run_simulation(
    run_duration: Optional[float] = Query(100.0, description="simulation run duration"),
    iat_mean: Optional[float] = Query(
        1.0, description="mean inter-arrival time (exponential distribution)"
    ),
    pt_mean: Optional[float] = Query(
        1.0, description="mean processing time (exponential distribution)"
    ),
    n_replications: Optional[int] = Query(
        1, description="number of replications for the simulation run"
    ),
):
    """
    Endpoint to run the simulation.

    Query Parameters:
    - run_duration: float = 100.0
        Simulation run duration.
    - iat_mean: float = 1.0
        Mean inter-arrival time (exponential distribution).
    - pt_mean: float = 1.0
        Mean processing time (exponential distribution).
    - n_replications: int = 1
        Number of replications for the simulation run.

    Returns:
    JSON response with KPIs and time series data.
    """
    return [
        {
            "replication_nr": i + 1,
            **simulate(
                run_duration=run_duration,
                iat_mean=iat_mean,
                pt_mean=pt_mean,
            ),
        }
        for i in range(n_replications)
    ]


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
