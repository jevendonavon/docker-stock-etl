# Start from official Python image
FROM python:3.12-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements first (for caching)
COPY requirements.txt .

# Install Python packages
RUN pip install -r requirements.txt

# Copy your ETL script
COPY etl.py .

# Run the ETL script when container starts
CMD ["python", "etl.py"]
