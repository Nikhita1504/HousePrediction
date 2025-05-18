# Correct base image
FROM python:3.7-slim

# Set working directory inside the container
WORKDIR /app

# Copy all project files into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port (Render uses $PORT)
EXPOSE $PORT

# Run the app
CMD ["gunicorn", "--bind", "0.0.0.0:$PORT", "app:app"]
