# Use Python 3.11 instead of 3.7
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements.txt first for better Docker layer caching
COPY requirements.txt .

# Upgrade pip and install dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files into the container
COPY . /app

# Expose port (Render uses $PORT)
EXPOSE 5000

# Run the app
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]