FROM python:3.10-slim

WORKDIR /backend

COPY /apps/backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY /apps/backend .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]