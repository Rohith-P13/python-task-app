# 1. Base Linux image with Python pre-installed
FROM python:3.11-slim

# 2. Set directory inside container
WORKDIR /app

# 3. Copy requirements list and install libraries
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy the application code
COPY main.py .

# 5. Tell Docker the container communicates through port 8000
EXPOSE 8000

# 6. Start the web server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]