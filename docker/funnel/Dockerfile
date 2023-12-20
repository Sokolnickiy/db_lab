FROM python:3.10

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

WORKDIR /app/funnel

ENTRYPOINT ["python", "main.py"]

