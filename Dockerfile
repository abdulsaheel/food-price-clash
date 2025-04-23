# Base image
FROM python:3.10-slim

# Set working dir
WORKDIR /app

# Install system deps
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    xvfb \
    libnss3 \
    libatk-bridge2.0-0 \
    libxss1 \
    libasound2 \
    fonts-liberation \
    libappindicator3-1 \
    libgbm-dev \
    libxshmfence1 \
    libgtk-3-0 \
    && rm -rf /var/lib/apt/lists/*

# Install Python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright and its dependencies
RUN pip install playwright && playwright install chromium

# Copy the app files
COPY . .

# Make the script executable
RUN chmod +x start.sh

# Expose FastAPI port
EXPOSE 8000

# Run the script
CMD ["./start.sh"]
