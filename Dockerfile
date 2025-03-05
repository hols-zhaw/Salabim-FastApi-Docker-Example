# Use an official Python base image
FROM python:3.11-slim

# Set environment variables
#  Prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
#  Ensure logs are sent directly to the terminal without buffering
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the FastAPI app code into the container
COPY ./app /app

# Expose the port the app runs on
EXPOSE 8000

# Command to run the FastAPI app using Uvicorn without hot reloading
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
