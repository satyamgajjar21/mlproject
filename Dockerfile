# Use lightweight Python image
FROM python:3.9-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements first (better caching)
COPY . /app

# Install system dependencies (for numpy, scipy etc.)
RUN apt update -y && apt install awscli -y

RUN pip install -r requirements.txt
CMD ["python3", "application.py"]
  