# MedBot Docker Image
FROM python:3.10-slim-buster

WORKDIR /app

COPY . /app

# Install CPU-only PyTorch first (saves ~1.5GB vs full torch)
RUN pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu

# Install remaining dependencies
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "app.py"]