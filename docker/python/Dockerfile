FROM python:3.10-slim

WORKDIR /backend

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

COPY apps/backend/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY apps/backend ./

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]