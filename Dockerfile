FROM python:3.12.7-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY procesar.py .

RUN useradd --create-home appuser \
    && mkdir -p /data/input /data/output \
    && chown -R appuser:appuser /data /app

ENV INPUT_PATH=/data/input/train.csv \
    OUTPUT_PATH=/data/output/titanic_limpio.csv \
    STATS_PATH=/data/output/estadisticas.csv

USER appuser

CMD ["python", "procesar.py"]