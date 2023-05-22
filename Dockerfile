FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 3001

CMD ["gunicorn", "--bind", "0.0.0.0:3001", "app:app"]