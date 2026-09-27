# 1. Start from a lightweight Linux environment with Python 3.11 pre-installed
FROM python:3.11-slim

# 2. Create a working folder inside the container
WORKDIR /app

# 3. Copy our local Python script into the container
COPY main.py .

# 4. Command to run when the container starts
CMD ["python", "main.py"]