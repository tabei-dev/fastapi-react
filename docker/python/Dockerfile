FROM python:3.13-slim

WORKDIR /backend

RUN apt update && apt install -y \
    build-essential \
    libpq-dev \
    make \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

COPY apps/backend/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY apps/backend ./

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]