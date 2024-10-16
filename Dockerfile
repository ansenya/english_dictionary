FROM python:3.13.0-alpine3.20

WORKDIR /app

COPY requirments.txt .

RUN apk add --no-cache python3-dev mariadb-dev build-base && \
    pip install --no-cache-dir -r requirments.txt && \
    pip install --no-cache-dir uvicorn

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
