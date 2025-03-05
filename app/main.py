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
        100.0, description="mean processing time (exponential distribution)"
    ),
):
    """
    Endpoint to run the simulation.

    Query Parameters:
    - run_duration: float = 100.0
        Simulation run duration.
    - iat_mean: float = 1.0
        Mean inter-arrival time (exponential distribution).
    - pt_mean: float = None
        Mean processing time (exponential distribution).

    Returns:
    JSON response with KPIs and time series data.
    """
    # Prepare keyword arguments for the simulate function
    simulation_params = {
        "run_duration": run_duration,
        "iat_mean": iat_mean,
        "pt_mean": pt_mean,
    }

    # Call the simulate function
    result = simulate(**simulation_params)

    return result


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
