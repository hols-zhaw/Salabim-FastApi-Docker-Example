# FastAPI App

A simple FastAPI application to demonstrate building and running a RESTful API. This guide includes instructions for both local development and Docker deployment.


## Table of Contents

1. [Local Development](#local-development)
   - Setting up the Python virtual environment
   - Running the application locally
2. [Docker Deployment](#docker-deployment)
   - Building the Docker image
   - Running the Docker container
   - Stopping the container
3. [Endpoints](#endpoints)


## Local Development

Follow these steps to run the FastAPI app on your local machine:

### 1. Prerequisites

Ensure you have the following installed:
- Python 3.11+
- pip (Python package installer)

### 2. Clone the Repository

```bash
git clone <repository-url>
cd fastapi-app
```

### 3. Set Up the Python Virtual Environment

Run the following commands to create and activate a virtual environment:

#### For macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### For Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 4. Install Dependencies

Install the required Python libraries:
```bash
python -m pip install -U pip
pip install -r requirements.txt
```

### 5. Run the Application

Start the FastAPI server locally:
```bash
uvicorn app.main:app --reload
```

The server will start at `http://127.0.0.1:8000`.

## Docker Deployment

You can containerize and run the application using Docker.

### 1. Prerequisites

Ensure Docker is installed and running on your machine.

- [Install Docker](https://docs.docker.com/get-docker/)


### 2. Build the Docker Image

From the project root directory, build the Docker image:

```bash
docker build -t fastapi-app .
```

### 3. Run the Docker Container

Run the container and map port 8000 to your host machine:

```bash
docker run -d -p 8000:8000 fastapi-app
```

The API will be available at:
```
http://127.0.0.1:8000
```

### 4. Stop the Docker Container

Find the container ID and stop it:

```bash
docker ps           # List running containers
docker stop <container_id>
```

To stop and remove all containers in one step (optional):
```bash
docker rm -f $(docker ps -aq)
```

## Endpoints

| Method | Endpoint      | Description                   |
|--------|---------------|-------------------------------|
| GET    | `/`           | Returns a welcome message.    |

Example Response:
```json
{
  "message": "Hello from FastAPI in Docker!"
}
```

## Next Steps

- Add more endpoints to expand functionality.
- Integrate a database like SQLite, PostgreSQL, or MongoDB.
- Deploy the application to a cloud provider (e.g., AWS, Azure, or Heroku).


## License

This project is licensed under the MIT License.
